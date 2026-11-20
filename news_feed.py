"""
news_feed.py - Google News RSS feed fetcher and parser for NewsHub.
Supports regional editions, category topics, and custom keyword searches.
"""

import requests
import xml.etree.ElementTree as ET
import email.utils
import datetime
import re
import urllib.parse
import streamlit as st

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def parse_relative_time(pub_date_str: str) -> str:
    """Converts RFC 2822 date string into a friendly relative timestamp."""
    if not pub_date_str:
        return ""
    try:
        dt = email.utils.parsedate_to_datetime(pub_date_str)
        now = datetime.datetime.now(datetime.timezone.utc)
        diff_seconds = (now - dt).total_seconds()
        
        if diff_seconds < 60:
            return "Just now"
        elif diff_seconds < 3600:
            mins = int(diff_seconds // 60)
            return f"{mins}m ago"
        elif diff_seconds < 86400:
            hours = int(diff_seconds // 3600)
            return f"{hours}h ago"
        elif diff_seconds < 172800:
            return "Yesterday"
        else:
            days = int(diff_seconds // 86400)
            if days <= 7:
                return f"{days}d ago"
            return dt.strftime("%b %d, %Y")
    except Exception:
        return pub_date_str

def clean_html_text(raw_html: str) -> str:
    """Strips HTML tags and normalizes whitespace."""
    if not raw_html:
        return ""
    clean = re.sub(r"<[^>]+>", " ", raw_html)
    clean = re.sub(r"&nbsp;", " ", clean)
    clean = re.sub(r"&amp;", "&", clean)
    clean = re.sub(r"&quot;", '"', clean)
    clean = re.sub(r"&#39;", "'", clean)
    clean = re.sub(r"&lt;", "<", clean)
    clean = re.sub(r"&gt;", ">", clean)
    return " ".join(clean.split())

@st.cache_data(ttl=180, show_spinner=False)
def fetch_google_news(
    topic: str = None, 
    query: str = None, 
    region_config: dict = None, 
    limit: int = 30
) -> list:
    """
    Fetches latest news from Google News RSS feeds.
    
    Args:
        topic: Google News section topic (WORLD, BUSINESS, TECHNOLOGY, etc.)
        query: Custom keyword search string
        region_config: Dictionary containing region params like hl, gl, ceid or query
        limit: Max number of items to return
    """
    if region_config is None:
        region_config = {"hl": "en-US", "gl": "US", "ceid": "US:en"}

    hl = region_config.get("hl", "en-US")
    gl = region_config.get("gl", "US")
    ceid = region_config.get("ceid", "US:en")

    # 1. Custom keyword search
    if query and query.strip():
        encoded_query = urllib.parse.quote(query.strip())
        rss_url = f"https://news.google.com/rss/search?q={encoded_query}&hl={hl}&gl={gl}&ceid={ceid}"
    
    # 2. Topic section (e.g. WORLD, TECHNOLOGY)
    elif topic:
        rss_url = f"https://news.google.com/rss/headlines/section/topic/{topic}?hl={hl}&gl={gl}&ceid={ceid}"
        
    # 3. Regional / Top Stories
    elif "query" in region_config:
        encoded_query = urllib.parse.quote(region_config["query"])
        rss_url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-US&gl=US&ceid=US:en"
    else:
        rss_url = f"https://news.google.com/rss?hl={hl}&gl={gl}&ceid={ceid}"

    articles = []
    try:
        resp = requests.get(rss_url, headers=HEADERS, timeout=6)
        if resp.status_code == 200:
            root = ET.fromstring(resp.content)
            channel = root.find("channel")
            if channel is not None:
                items = channel.findall("item")
                for item in items[:limit]:
                    raw_title = item.findtext("title") or "Untitled Story"
                    link = item.findtext("link") or "#"
                    pub_date = item.findtext("pubDate") or ""
                    source_elem = item.find("source")
                    source_name = source_elem.text.strip() if (source_elem is not None and source_elem.text) else ""

                    # Clean headline title
                    clean_title = raw_title.strip()
                    if source_name and clean_title.endswith(f" - {source_name}"):
                        clean_title = clean_title[:-len(f" - {source_name}")].strip()
                    elif " - " in clean_title:
                        parts = clean_title.rsplit(" - ", 1)
                        if not source_name:
                            source_name = parts[1].strip()
                        clean_title = parts[0].strip()

                    if not source_name:
                        source_name = "Google News"

                    raw_desc = item.findtext("description") or ""
                    clean_desc = clean_html_text(raw_desc)
                    # If description is identical to title or contains source names only, provide excerpt
                    if clean_desc.startswith(clean_title):
                        remaining = clean_desc[len(clean_title):].strip()
                        if remaining:
                            clean_desc = remaining
                    
                    time_ago = parse_relative_time(pub_date)

                    articles.append({
                        "title": clean_title,
                        "source": source_name,
                        "link": link,
                        "pub_date": pub_date,
                        "time_ago": time_ago,
                        "description": clean_desc[:250] + ("..." if len(clean_desc) > 250 else "")
                    })
    except Exception as e:
        # Graceful fallback on network or parsing error
        pass

    return articles
