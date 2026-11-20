"""
NewsHub - 24/7 Global Live Streams & Breaking News Feed
An enhanced multimedia news platform pairing international live broadcast streams with real-time Google News article feeds.
"""

import streamlit as st
import streamlit.components.v1 as components
import random
from typing import Optional

from channels_data import (
    CHANNELS_BY_REGION, 
    ALL_CHANNELS, 
    REGION_TO_GOOGLE_NEWS, 
    GOOGLE_NEWS_TOPICS
)
from streams import (
    fetch_latest_live_video_id, 
    get_all_channel_statuses, 
    get_embed_player_html
)
from news_feed import fetch_google_news
from styles import CUSTOM_CSS

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="NewsHub | 24/7 Global Live Streams & Breaking News",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- 2. SESSION STATE INITIALIZATION ---
if "current_country" not in st.session_state:
    st.session_state.current_country = "All"

if "current_channel" not in st.session_state:
    st.session_state.current_channel = list(ALL_CHANNELS.keys())[0]

if "view_mode" not in st.session_state:
    st.session_state.view_mode = "📺 Split View (Stream + Articles)"

if "news_topic" not in st.session_state:
    st.session_state.news_topic = "🔥 Top Stories"

if "news_search_query" not in st.session_state:
    st.session_state.news_search_query = ""

if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = {}  # {url: {title, source, time_ago}}

if "auto_sync_news" not in st.session_state:
    st.session_state.auto_sync_news = True

if "force_channel_embed" not in st.session_state:
    st.session_state.force_channel_embed = False


# --- 3. STATE CALLBACKS & HELPERS ---
def on_country_change():
    sel_country = st.session_state.current_country
    if sel_country == "All":
        st.session_state.current_channel = list(ALL_CHANNELS.keys())[0]
    else:
        region_channels = list(CHANNELS_BY_REGION.get(sel_country, {}).keys())
        if region_channels:
            st.session_state.current_channel = region_channels[0]

def set_channel(channel_name: str):
    st.session_state.current_channel = channel_name

def toggle_bookmark(title: str, link: str, source: str, time_ago: str):
    if link in st.session_state.bookmarks:
        del st.session_state.bookmarks[link]
    else:
        st.session_state.bookmarks[link] = {
            "title": title,
            "source": source,
            "time_ago": time_ago,
            "link": link
        }

def pick_random_channel(live_only: bool = False, statuses: dict = None):
    candidates = list(ALL_CHANNELS.keys())
    if live_only and statuses:
        live_candidates = [name for name in candidates if statuses.get(name, {}).get("is_live")]
        if live_candidates:
            candidates = live_candidates
    new_choice = random.choice(candidates)
    st.session_state.current_channel = new_choice
    st.session_state.current_country = ALL_CHANNELS[new_choice].get("region", "All")


# Fetch channel statuses (cached for 60s)
channel_statuses = get_all_channel_statuses(ALL_CHANNELS)
live_count = sum(1 for s in channel_statuses.values() if s.get("is_live"))
total_channels = len(ALL_CHANNELS)


# --- 4. TOP BRANDING & BREAKING NEWS TICKER ---
top_col1, top_col2 = st.columns([3, 1])

with top_col1:
    st.markdown(
        f"""
        <div class="newshub-header-container">
            <div class="newshub-logo">
                <span class="newshub-logo-badge">NEWSHUB</span>
                <div>
                    <h1 class="newshub-title">Global Broadcast Directory & Google News Feed</h1>
                    <p class="newshub-subtitle">Real-time international live streams paired with synced Google News article feeds</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with top_col2:
    st.markdown(
        f"""
        <div style="display: flex; gap: 8px; justify-content: flex-end; align-items: center; height: 100%; padding-top: 10px;">
            <div class="live-pill">
                <span class="live-dot"></span>
                {live_count} LIVE NOW
            </div>
            <div class="stat-pill">
                📡 {total_channels} CHANNELS
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Breaking News Ticker from Google News
ticker_headlines = fetch_google_news(limit=6)
if ticker_headlines:
    ticker_links = " &nbsp;&nbsp;•&nbsp;&nbsp; ".join([
        f'<a href="{item["link"]}" target="_blank"><strong>[{item["source"]}]</strong> {item["title"]}</a> <span style="opacity:0.6; font-size:0.8em;">({item["time_ago"]})</span>'
        for item in ticker_headlines
    ])
    st.markdown(
        f"""
        <div class="ticker-wrapper">
            <span class="ticker-badge">⚡ BREAKING</span>
            <div class="ticker-content">
                {ticker_links}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# --- 5. TOP NAVIGATION & CONTROL BAR ---
nav_c1, nav_c2, nav_c3, nav_c4 = st.columns([1.5, 2.2, 1.6, 1.7])

with nav_c1:
    region_list = ["All"] + list(CHANNELS_BY_REGION.keys())
    st.selectbox(
        "🌎 Region / Edition",
        options=region_list,
        key="current_country",
        on_change=on_country_change
    )

with nav_c2:
    # Get available channels based on region
    if st.session_state.current_country == "All":
        available_channels = list(ALL_CHANNELS.keys())
    else:
        available_channels = list(CHANNELS_BY_REGION.get(st.session_state.current_country, {}).keys())
    
    # Ensure current channel is in available list
    if st.session_state.current_channel not in available_channels and available_channels:
        st.session_state.current_channel = available_channels[0]

    def format_channel_choice(name):
        info = channel_statuses.get(name, {})
        icon = "🟢" if info.get("is_live") else "⚪"
        return f"{icon} {name}"

    st.selectbox(
        "📡 Broadcast Channel",
        options=available_channels,
        key="current_channel",
        format_func=format_channel_choice
    )

with nav_c3:
    topic_choice = st.selectbox(
        "📰 News Topic",
        options=list(GOOGLE_NEWS_TOPICS.keys()),
        key="news_topic"
    )

with nav_c4:
    st.selectbox(
        "🖥️ Layout View",
        options=[
            "📺 Split View (Stream + Articles)",
            "🎥 Cinema Mode (Stream Focused)",
            "📰 Newsstand (Articles Focused)"
        ],
        key="view_mode"
    )


# --- 6. SIDEBAR CONTROLS & DIRECTORY ---
with st.sidebar:
    st.markdown("### 🌐 NewsHub Control Center")
    
    # Quick Random Broadcast Discovery
    rand_c1, rand_c2 = st.columns(2)
    with rand_c1:
        if st.button("🎲 Any Stream", use_container_width=True, help="Pick a random channel"):
            pick_random_channel(live_only=False, statuses=channel_statuses)
            st.rerun()
    with rand_c2:
        if st.button("🟢 Live Only", use_container_width=True, help="Pick a channel currently broadcasting live"):
            pick_random_channel(live_only=True, statuses=channel_statuses)
            st.rerun()

    st.divider()

    # Regional News Auto-sync toggle
    st.session_state.auto_sync_news = st.toggle(
        "🔗 Sync News to Selected Region",
        value=st.session_state.auto_sync_news,
        help="When enabled, Google News automatically loads articles from the region selected in the top dropdown."
    )

    st.session_state.force_channel_embed = st.checkbox(
        "Force Native Channel Embed",
        value=st.session_state.force_channel_embed,
        help="Use YouTube's direct live_stream embed player instead of detected video ID."
    )

    st.divider()

    # Reading List / Bookmarks drawer
    st.markdown(f"### 📌 Reading List ({len(st.session_state.bookmarks)})")
    if st.session_state.bookmarks:
        for b_link, b_info in list(st.session_state.bookmarks.items()):
            with st.container():
                st.markdown(f"**[{b_info['title']}]({b_link})**")
                sub_c1, sub_c2 = st.columns([2, 1])
                with sub_c1:
                    st.caption(f"{b_info['source']} • {b_info['time_ago']}")
                with sub_c2:
                    if st.button("✕ Remove", key=f"del_bm_{b_link[:25]}", use_container_width=True):
                        del st.session_state.bookmarks[b_link]
                        st.rerun()
        if st.button("🗑️ Clear All Bookmarks", use_container_width=True):
            st.session_state.bookmarks.clear()
            st.rerun()
    else:
        st.caption("No bookmarked articles yet. Click '⭐ Save' on any news article card to save it here.")

    st.divider()

    # Architecture info note
    with st.expander("ℹ️ About NewsHub Architecture"):
        st.markdown(
            """
            **NewsHub** unites two public feeds with zero paid API keys:
            1. **YouTube RSS (`UULV`)**: Queries public Atom/XML feeds for channel live broadcasts via concurrent workers.
            2. **Google News RSS**: Real-time structured regional & topical article feeds with automated clean snippet parsing.
            3. **Resilient Fallback**: Auto-routes to direct channel stream embeds when broadcasters rotate or gate IDs.
            """
        )


# --- 7. HELPER FUNCTIONS TO RENDER COMPONENTS ---

def render_video_player(height: int = 560):
    """Renders the active live video player, channel metadata, and quick action buttons."""
    active_channel = st.session_state.current_channel
    channel_info = ALL_CHANNELS.get(active_channel, {})
    cid = channel_info.get("id")
    
    status_info = channel_statuses.get(active_channel, {})
    is_live = status_info.get("is_live", False)
    detected_video_id = status_info.get("video_id")
    video_title = status_info.get("video_title")

    # Header above player
    h_c1, h_c2 = st.columns([3, 1])
    with h_c1:
        st.markdown(f"### {active_channel}")
        if video_title:
            st.caption(f"📺 {video_title}")
        elif channel_info.get("desc"):
            st.caption(f"{channel_info.get('desc')}")
    with h_c2:
        if is_live:
            st.markdown(
                '<div style="text-align: right;"><span class="live-pill"><span class="live-dot"></span> LIVE BROADCAST</span></div>', 
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div style="text-align: right;"><span class="standby-pill">⚪ DIRECT STREAM</span></div>', 
                unsafe_allow_html=True
            )

    # Embed Player
    if cid:
        use_video_id = None if st.session_state.force_channel_embed else detected_video_id
        iframe_code = get_embed_player_html(
            channel_name=active_channel,
            channel_id=cid,
            video_id=use_video_id,
            height=height
        )
        components.html(iframe_code, height=height + 15)
        
        # Player control bar underneath
        btn_c1, btn_c2, btn_c3, btn_c4 = st.columns([1.5, 1.5, 1.2, 1.2])
        with btn_c1:
            youtube_live_url = f"https://www.youtube.com/channel/{cid}/live"
            st.link_button("↗ Watch on YouTube Live", youtube_live_url, use_container_width=True)
        with btn_c2:
            if detected_video_id:
                yt_video_url = f"https://www.youtube.com/watch?v={detected_video_id}"
                st.link_button("🎬 Open Video Directly", yt_video_url, use_container_width=True)
            else:
                st.button("🔄 Refresh Stream Check", use_container_width=True, on_click=lambda: st.cache_data.clear())
        with btn_c3:
            st.caption(f"Region: **{channel_info.get('region', 'Global')}**")
        with btn_c4:
            st.caption(f"Category: **{channel_info.get('category', 'News')}**")
    else:
        st.warning(f"Channel ID not configured for {active_channel}.")


@st.fragment(run_every="60s")
def render_channel_drawer():
    """Silent auto-refreshing side directory that keeps live dots updated every 60s."""
    current_region = st.session_state.current_country
    if current_region == "All":
        target_dict = ALL_CHANNELS
        label = "Global Channel Directory"
    else:
        target_dict = CHANNELS_BY_REGION.get(current_region, {})
        label = f"{current_region} Channels"

    statuses = get_all_channel_statuses(ALL_CHANNELS)
    region_live = sum(1 for ch in target_dict.keys() if statuses.get(ch, {}).get("is_live"))

    st.markdown(f"#### 📡 {label}")
    st.markdown(f"<p style='color: #8b949e; font-size: 0.82em;'>🟢 {region_live} Live Now &nbsp;|&nbsp; ⚪ {len(target_dict) - region_live} Standby</p>", unsafe_allow_html=True)

    for ch_name in target_dict.keys():
        is_active = (ch_name == st.session_state.current_channel)
        is_live = statuses.get(ch_name, {}).get("is_live", False)
        
        icon = "🟢" if is_live else "⚪"
        btn_text = f"{icon}  {ch_name}"
        if is_active:
            btn_text = f"▶  {btn_text}"

        if st.button(
            btn_text, 
            key=f"drawer_btn_{ch_name}", 
            use_container_width=True, 
            type="primary" if is_active else "secondary"
        ):
            set_channel(ch_name)
            st.rerun()


def render_news_feed_column(limit: int = 25):
    """Renders the real-time Google News feed with search, topic filtering, and article cards."""
    # Search input
    s_col1, s_col2 = st.columns([3.5, 1])
    with s_col1:
        search_val = st.text_input(
            "Search Breaking News", 
            value=st.session_state.news_search_query,
            placeholder="Search keywords, companies, leaders...",
            label_visibility="collapsed"
        )
        if search_val != st.session_state.news_search_query:
            st.session_state.news_search_query = search_val
            st.rerun()
    with s_col2:
        if st.session_state.news_search_query:
            if st.button("✕ Clear", use_container_width=True):
                st.session_state.news_search_query = ""
                st.rerun()

    # Determine region config
    region_cfg = None
    if st.session_state.auto_sync_news and not st.session_state.news_search_query:
        region_cfg = REGION_TO_GOOGLE_NEWS.get(st.session_state.current_country)

    topic_key = GOOGLE_NEWS_TOPICS.get(st.session_state.news_topic)

    # Fetch articles
    articles = fetch_google_news(
        topic=topic_key,
        query=st.session_state.news_search_query if st.session_state.news_search_query.strip() else None,
        region_config=region_cfg,
        limit=limit
    )

    # Feed header info
    f_info1, f_info2 = st.columns([2, 1])
    with f_info1:
        if st.session_state.news_search_query:
            st.markdown(f"**Search Results:** `{st.session_state.news_search_query}`")
        else:
            region_label = st.session_state.current_country if st.session_state.auto_sync_news else "Global"
            st.markdown(f"**{st.session_state.news_topic}** &nbsp;•&nbsp; <span style='color: #8b949e; font-size: 0.85em;'>Region: {region_label} ({len(articles)} articles)</span>", unsafe_allow_html=True)
    with f_info2:
        if st.button("🔄 Refresh Feed", key="refresh_news_btn", use_container_width=True):
            st.cache_data.clear()
            st.rerun()

    if not articles:
        st.info("No matching articles found. Try searching another topic or check your network connection.")
        return

    # Render scrollable article list
    with st.container(height=650):
        for idx, art in enumerate(articles):
            is_bookmarked = art["link"] in st.session_state.bookmarks
            bm_btn_label = "★ Saved" if is_bookmarked else "☆ Save"

            st.markdown(
                f"""
                <div class="article-card">
                    <div class="article-header">
                        <span class="source-badge">{art['source']}</span>
                        <span class="time-badge">{art['time_ago']}</span>
                    </div>
                    <div class="article-title">
                        <a href="{art['link']}" target="_blank">{art['title']}</a>
                    </div>
                    {f'<div class="article-snippet">{art["description"]}</div>' if art.get("description") else ''}
                    <div class="article-footer">
                        <a href="{art['link']}" target="_blank" class="read-btn">Read Full Story ↗</a>
                        <span style="font-size: 0.72em; color: #6e7681;">Google News RSS</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            # Bookmark button directly under each card
            b_c1, b_c2 = st.columns([4, 1])
            with b_c2:
                if st.button(bm_btn_label, key=f"feed_bm_{idx}_{art['link'][:20]}", use_container_width=True):
                    toggle_bookmark(art["title"], art["link"], art["source"], art["time_ago"])
                    st.rerun()


# --- 8. MAIN VIEW ROUTING ---

if st.session_state.view_mode == "📺 Split View (Stream + Articles)":
    # 2-column layout: Left = Player + Drawer; Right = Google News Feed
    col_left, col_right = st.columns([13, 9], gap="large")

    with col_left:
        render_video_player(height=520)
        st.divider()
        with st.container(height=360):
            render_channel_drawer()

    with col_right:
        st.markdown("### 📰 Google News Live Stream")
        render_news_feed_column(limit=30)

elif st.session_state.view_mode == "🎥 Cinema Mode (Stream Focused)":
    # Wide cinema player taking full width
    render_video_player(height=640)
    
    st.divider()
    cin_col1, cin_col2 = st.columns([1, 2], gap="large")
    with cin_col1:
        with st.container(height=450):
            render_channel_drawer()
    with cin_col2:
        st.markdown("### 📰 Breaking Headlines")
        render_news_feed_column(limit=15)

elif st.session_state.view_mode == "📰 Newsstand (Articles Focused)":
    # Dedicated magazine/newspaper layout
    st.markdown("## 📰 The Global Newsstand")
    st.caption("Powered by Google News real-time RSS feeds, filtered across regional editions and topics.")

    # Search & filters
    ns_c1, ns_c2 = st.columns([3, 1])
    with ns_c1:
        st.session_state.news_search_query = st.text_input(
            "Search all topics", 
            value=st.session_state.news_search_query,
            placeholder="Search breaking stories, geopolitics, AI, markets..."
        )
    with ns_c2:
        st.session_state.news_topic = st.selectbox(
            "Filter Category",
            options=list(GOOGLE_NEWS_TOPICS.keys()),
            key="ns_topic_sel"
        )

    region_cfg = REGION_TO_GOOGLE_NEWS.get(st.session_state.current_country) if st.session_state.auto_sync_news else None
    topic_key = GOOGLE_NEWS_TOPICS.get(st.session_state.news_topic)
    articles = fetch_google_news(
        topic=topic_key,
        query=st.session_state.news_search_query if st.session_state.news_search_query.strip() else None,
        region_config=region_cfg,
        limit=36
    )

    if not articles:
        st.info("No articles found.")
    else:
        # 3-column card grid
        grid_cols = st.columns(3, gap="medium")
        for i, art in enumerate(articles):
            col_target = grid_cols[i % 3]
            with col_target:
                is_bm = art["link"] in st.session_state.bookmarks
                bm_icon = "★ Saved" if is_bm else "☆ Save"
                st.markdown(
                    f"""
                    <div class="article-card" style="min-height: 220px; display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <div class="article-header">
                                <span class="source-badge">{art['source']}</span>
                                <span class="time-badge">{art['time_ago']}</span>
                            </div>
                            <div class="article-title">
                                <a href="{art['link']}" target="_blank">{art['title']}</a>
                            </div>
                            <div class="article-snippet">{art.get('description', '')}</div>
                        </div>
                        <div class="article-footer">
                            <a href="{art['link']}" target="_blank" class="read-btn">Read Story ↗</a>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button(bm_icon, key=f"grid_bm_{i}_{art['link'][:15]}", use_container_width=True):
                    toggle_bookmark(art["title"], art["link"], art["source"], art["time_ago"])
                    st.rerun()

# --- 9. FOOTER ---
st.divider()
st.markdown(
    """
    <div style="text-align: center; color: #8b949e; font-size: 0.85em; padding: 1rem 0;">
        <strong>NewsHub</strong> — Built with Streamlit, YouTube RSS, and Google News RSS Feeds.<br>
        Free, open news aggregation without tracking or paywalls. All broadcasts and articles belong to their respective publishers.
    </div>
    """,
    unsafe_allow_html=True
)
