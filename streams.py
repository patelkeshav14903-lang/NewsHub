"""
streams.py - YouTube RSS live stream detector and video player utilities for NewsHub.
"""

import requests
import xml.etree.ElementTree as ET
import concurrent.futures
import streamlit as st
from typing import Optional, Tuple, Dict, Any

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_latest_live_video_id(channel_id: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Fetches the video ID and title of an active live stream via YouTube's UULV playlist RSS.
    
    Returns:
        (video_id, video_title) or (None, None)
    """
    if not channel_id or not channel_id.startswith("UC"):
        return None, None

    playlist_id = "UULV" + channel_id[2:]
    rss_url = f"https://www.youtube.com/feeds/videos.xml?playlist_id={playlist_id}"

    try:
        response = requests.get(rss_url, headers=HEADERS, timeout=4)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            atom_ns = "{http://www.w3.org/2005/Atom}"
            yt_ns = {"yt": "http://www.youtube.com/xml/schemas/2015"}

            entry = root.find(f"{atom_ns}entry")
            if entry is not None:
                video_id_elem = entry.find("yt:videoId", yt_ns)
                title_elem = entry.find(f"{atom_ns}title")
                vid = video_id_elem.text if video_id_elem is not None else None
                title = title_elem.text if title_elem is not None else None
                return vid, title
    except Exception:
        pass

    return None, None

@st.cache_data(ttl=60, show_spinner=False)
def get_all_channel_statuses(channel_dict: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """
    Pings channels concurrently using ThreadPoolExecutor to determine live broadcast status.
    Cached for 60 seconds via @st.cache_data.
    """
    results = {}

    def check_channel(name: str, info: dict):
        cid = info.get("id")
        video_id, video_title = fetch_latest_live_video_id(cid)
        is_live = bool(video_id)
        return name, {
            "is_live": is_live,
            "video_id": video_id,
            "video_title": video_title,
            "channel_id": cid
        }

    with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
        futures = [executor.submit(check_channel, name, info) for name, info in channel_dict.items()]
        for future in concurrent.futures.as_completed(futures):
            try:
                name, status_data = future.result()
                results[name] = status_data
            except Exception:
                pass

    return results

def get_embed_player_html(
    channel_name: str,
    channel_id: str,
    video_id: Optional[str] = None,
    height: int = 580
) -> str:
    """
    Generates a responsive, modern HTML5 iframe for the YouTube live broadcast.
    Uses video_id if available, otherwise falls back to YouTube's live_stream channel player.
    """
    if video_id:
        embed_src = f"https://www.youtube-nocookie.com/embed/{video_id}?autoplay=1&mute=0&rel=0&modestbranding=1"
    else:
        # Fallback to direct channel live embed
        embed_src = f"https://www.youtube-nocookie.com/embed/live_stream?channel={channel_id}&autoplay=1&mute=0"

    html = f"""
    <div style="position: relative; width: 100%; border-radius: 14px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.35); background: #0b0f19;">
        <iframe 
            width="100%" 
            height="{height}" 
            src="{embed_src}" 
            title="{channel_name} Live Broadcast" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen
            style="display: block; width: 100%; border: none;">
        </iframe>
    </div>
    """
    return html
