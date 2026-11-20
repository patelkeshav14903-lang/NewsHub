"""
styles.py - Custom CSS animations, badges, and layout aesthetics for NewsHub.
"""

CUSTOM_CSS = """
<style>
/* Modern typography and font smoothing */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

/* Header branding */
.newshub-header-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.5rem 0 1rem 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 1rem;
}

.newshub-logo {
    display: flex;
    align-items: center;
    gap: 12px;
}

.newshub-logo-badge {
    background: linear-gradient(135deg, #FF0055 0%, #FF5500 100%);
    color: white;
    font-weight: 800;
    font-size: 1.15rem;
    padding: 6px 14px;
    border-radius: 8px;
    letter-spacing: 0.5px;
    box-shadow: 0 4px 15px rgba(255, 0, 85, 0.35);
}

.newshub-title {
    font-size: 1.6rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    margin: 0;
    line-height: 1.2;
}

.newshub-subtitle {
    font-size: 0.88rem;
    color: #8b949e;
    margin: 2px 0 0 0;
}

/* Pulsing Live indicator */
.live-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(239, 68, 68, 0.15);
    color: #ef4444;
    border: 1px solid rgba(239, 68, 68, 0.35);
    font-size: 0.75rem;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 20px;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}

.live-dot {
    width: 8px;
    height: 8px;
    background-color: #ef4444;
    border-radius: 50%;
    animation: livePulse 1.6s infinite ease-in-out;
}

@keyframes livePulse {
    0% {
        transform: scale(0.9);
        box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7);
    }
    70% {
        transform: scale(1.2);
        box-shadow: 0 0 0 7px rgba(239, 68, 68, 0);
    }
    100% {
        transform: scale(0.9);
        box-shadow: 0 0 0 0 rgba(239, 68, 68, 0);
    }
}

.standby-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(148, 163, 184, 0.12);
    color: #94a3b8;
    border: 1px solid rgba(148, 163, 184, 0.25);
    font-size: 0.75rem;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 20px;
}

/* Breaking News Ticker bar */
.ticker-wrapper {
    background: rgba(22, 27, 34, 0.85);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    padding: 8px 14px;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    overflow: hidden;
    gap: 12px;
}

.ticker-badge {
    background: #e11d48;
    color: white;
    font-size: 0.72rem;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 5px;
    letter-spacing: 0.6px;
    white-space: nowrap;
    text-transform: uppercase;
}

.ticker-content {
    display: inline-block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-size: 0.88rem;
    color: #c9d1d9;
}

.ticker-content a {
    color: inherit;
    text-decoration: none;
    transition: color 0.2s ease;
}

.ticker-content a:hover {
    color: #58a6ff;
    text-decoration: underline;
}

/* News Article Card */
.article-card {
    background: rgba(22, 27, 34, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 14px 16px;
    margin-bottom: 12px;
    transition: all 0.2s ease;
}

.article-card:hover {
    border-color: rgba(99, 102, 241, 0.4);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
    transform: translateY(-2px);
}

.article-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 6px;
}

.source-badge {
    display: inline-block;
    background: rgba(99, 102, 241, 0.15);
    color: #818cf8;
    border: 1px solid rgba(99, 102, 241, 0.3);
    font-size: 0.72rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 6px;
    letter-spacing: 0.3px;
}

.time-badge {
    font-size: 0.75rem;
    color: #8b949e;
}

.article-title {
    font-size: 0.96rem;
    font-weight: 600;
    line-height: 1.35;
    margin-bottom: 6px;
    color: #f0f6fc;
}

.article-title a {
    color: inherit;
    text-decoration: none;
}

.article-title a:hover {
    color: #58a6ff;
}

.article-snippet {
    font-size: 0.82rem;
    color: #8b949e;
    line-height: 1.4;
    margin-bottom: 10px;
}

.article-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 0.78rem;
    padding-top: 6px;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.read-btn {
    color: #58a6ff;
    text-decoration: none;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}

.read-btn:hover {
    text-decoration: underline;
    color: #79b8ff;
}

/* Stat pills */
.stat-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 10px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    font-size: 0.8rem;
    color: #c9d1d9;
}

/* Compact side menu buttons */
div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column;"] > div[data-testid="stButton"] button {
    text-align: left;
    justify-content: flex-start;
    padding: 0.45rem 0.85rem;
    border-radius: 8px;
}

/* Smooth custom scrollbars */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: transparent;
}
::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.15);
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.3);
}
</style>
"""
