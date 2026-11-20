"""
channels_data.py - Channel directory, metadata, and regional mapping for NewsHub.
"""

CHANNELS_BY_REGION = {
    "United States": {
        "NBC News NOW": {
            "id": "UCeY0bbntWzzVIaj2z3QigXg",
            "country": "United States",
            "category": "General News",
            "desc": "NBC News 24/7 streaming network covering breaking news and headlines."
        },
        "ABC News Live": {
            "id": "UCBi2mrWuNuyYy4gbM6fU18Q",
            "country": "United States",
            "category": "General News",
            "desc": "ABC News 24/7 live news channel with context, analysis, and breaking stories."
        },
        "CBS News Streaming": {
            "id": "UC8p1vwvWtl6T73JiExfWs1g",
            "country": "United States",
            "category": "General News",
            "desc": "CBS News 24/7 digital streaming news service."
        },
        "CNN": {
            "id": "UCupvZG-5ko_eiXAupbDfxWw",
            "country": "United States",
            "category": "General News",
            "desc": "Cable News Network - global breaking news, politics, and world events."
        },
        "Fox News": {
            "id": "UCXIJgqnII2ZOINSWNOGFThA",
            "country": "United States",
            "category": "General News",
            "desc": "Fox News Channel - breaking news, politics, and current affairs."
        },
        "LiveNOW from FOX": {
            "id": "UCJg9wBPyKMNA5sRDnvzmkdg",
            "country": "United States",
            "category": "Breaking News",
            "desc": "Raw, unfiltered, non-stop breaking news from FOX."
        },
        "MSNBC": {
            "id": "UCaXkIU1QidjPwiAYu6GcHjg",
            "country": "United States",
            "category": "Politics & Opinion",
            "desc": "MSNBC in-depth analysis and political commentary."
        },
        "PBS NewsHour": {
            "id": "UC6ZFN9Tx6xh-skXCuRHCDpQ",
            "country": "United States",
            "category": "In-Depth News",
            "desc": "Trusted, independent news reporting and analysis from PBS."
        },
        "Associated Press": {
            "id": "UC52X5wxj_VRyew03QzqByEw",
            "country": "United States",
            "category": "Wire Service",
            "desc": "Real-time updates from journalists around the globe."
        },
        "Bloomberg Television": {
            "id": "UCIALMKvObZNtJ6AmdCLP7Lg",
            "country": "United States",
            "category": "Business & Finance",
            "desc": "Global business, financial market data, and economic updates."
        },
        "CNBC": {
            "id": "UCvJJ_dzjViJCoLf5uKUTcgA",
            "country": "United States",
            "category": "Business & Finance",
            "desc": "First in business worldwide, market updates, and investment analysis."
        },
        "Yahoo Finance": {
            "id": "UCeioA5CXYLh63-B_eI91eFQ",
            "country": "United States",
            "category": "Markets",
            "desc": "Stock market coverage, crypto, and economic news."
        },
        "Forbes": {
            "id": "UCb75A1hEqKzGxw-Mlt9BfMQ",
            "country": "United States",
            "category": "Business",
            "desc": "Business, investing, technology, and leadership stories."
        },
        "Wall Street Journal": {
            "id": "UCK7tptYoggEXHI42YMEBNYQ",
            "country": "United States",
            "category": "Finance & Economics",
            "desc": "Original video journalism from WSJ newsrooms around the globe."
        },
        "Washington Post": {
            "id": "UCHd62jWAeH1_F2g5j2Tqwaw",
            "country": "United States",
            "category": "Politics & World",
            "desc": "Investigative journalism and political reporting."
        },
        "New York Times": {
            "id": "UCqnbDFdCpuN8CMEg0VuEBqA",
            "country": "United States",
            "category": "World & Culture",
            "desc": "Video journalism from The New York Times."
        },
        "USA Today": {
            "id": "UCP6HWOZyMAZdWMGLZI9XhZg",
            "country": "United States",
            "category": "General News",
            "desc": "National and global news updates from USA TODAY."
        },
        "NewsNation": {
            "id": "UCY-mD3sN7lJ17n-D8bM5-2g",
            "country": "United States",
            "category": "General News",
            "desc": "Unbiased, straightforward news reporting across America."
        },
        "C-SPAN": {
            "id": "UCb--64Gl51jIEVE-GLDAVTg",
            "country": "United States",
            "category": "Government & Congress",
            "desc": "Live, gavel-to-gavel coverage of US government and Congress."
        },
        "NASA": {
            "id": "UCLA_DiR1FfKNvjuUpBHmylQ",
            "country": "United States",
            "category": "Science & Space",
            "desc": "Live views from Earth orbit, rocket launches, and space exploration."
        }
    },
    "United Kingdom": {
        "BBC News": {
            "id": "UC16niRr50-MSBwiO3YDb3RA",
            "country": "United Kingdom",
            "category": "World News",
            "desc": "British Broadcasting Corporation - worldwide news reporting."
        },
        "Sky News": {
            "id": "UCoMdktPbSTixAyNGwb-PUkQ",
            "country": "United Kingdom",
            "category": "Breaking News",
            "desc": "First for breaking news, live video, and world headlines."
        },
        "GB News": {
            "id": "UCoOOsZA-XwI16G3yQ5BwB2Q",
            "country": "United Kingdom",
            "category": "News & Debate",
            "desc": "UK news channel featuring analysis, debate, and opinions."
        },
        "Reuters": {
            "id": "UChqUTb7kYRX8-EiaN3XFrSQ",
            "country": "United Kingdom",
            "category": "Global Wire",
            "desc": "Trusted, verified international breaking news from Reuters."
        },
        "The Telegraph": {
            "id": "UCPgLNge0xqQHWM5B5EFH9Cg",
            "country": "United Kingdom",
            "category": "News & Analysis",
            "desc": "British quality newspaper with video reporting and analysis."
        },
        "The Guardian": {
            "id": "UCryqIlX0R2K3xU_W2e8L4AQ",
            "country": "United Kingdom",
            "category": "Investigative",
            "desc": "Independent journalism with global coverage."
        },
        "The Sun": {
            "id": "UCIzXayRP7-P0ANpq-nD-h5g",
            "country": "United Kingdom",
            "category": "Tabloid & Breaking",
            "desc": "Breaking UK news, showbiz, and current events."
        },
        "Channel 4 News": {
            "id": "UCTzux-sWezQ3lS1xQ2C0mZw",
            "country": "United Kingdom",
            "category": "In-Depth Journalism",
            "desc": "Hard-hitting news, special reports, and investigative journalism."
        }
    },
    "Europe": {
        "Euronews English": {
            "id": "UC4JWaZokK7NjIlf2KF1HUMQ",
            "country": "Europe",
            "category": "Pan-European",
            "desc": "European perspective on international events and headlines."
        },
        "France 24 English": {
            "id": "UCCJQbp3MWqqAIE2L4-z1c6g",
            "country": "France",
            "category": "International",
            "desc": "International news broadcasting from Paris in English."
        },
        "DW News (Germany)": {
            "id": "UCknLrEdhRCp1aegoMqRaCEg",
            "country": "Germany",
            "category": "Global News",
            "desc": "Deutsche Welle - in-depth journalism from Berlin."
        },
        "TVP World": {
            "id": "UC6wFq9w0mQp0zS6F6L7hHpw",
            "country": "Poland / CEE",
            "category": "Central & Eastern Europe",
            "desc": "Central and Eastern European perspective on world news."
        }
    },
    "Middle East & Africa": {
        "Al Jazeera English": {
            "id": "UCNye-wNBqNL5ZzHSJj3l8Bg",
            "country": "Qatar",
            "category": "World & Middle East",
            "desc": "International news coverage with deep focus on the Global South."
        },
        "TRT World (Turkey)": {
            "id": "UC7fWeaHhqgM4Ry-RMpM2YYw",
            "country": "Turkey",
            "category": "Global News",
            "desc": "Turkish international public broadcaster."
        },
        "Africanews": {
            "id": "UCqGhtZAUIymDndXEq932Ojw",
            "country": "Pan-Africa",
            "category": "African News",
            "desc": "First pan-African multilingual news channel."
        },
        "SABC News (South Africa)": {
            "id": "UC8yH-uI81UUtEMDsowQyx1g",
            "country": "South Africa",
            "category": "African News",
            "desc": "South African Broadcasting Corporation 24/7 news stream."
        },
        "eNCA (South Africa)": {
            "id": "UCpswz-pD80YnQoA1oU_m-OQ",
            "country": "South Africa",
            "category": "African News",
            "desc": "Independent 24-hour South African television news."
        },
        "i24NEWS English": {
            "id": "UCvtp_A_OQn63c7uP5F2v_gA",
            "country": "Israel",
            "category": "Middle East News",
            "desc": "International 24-hour news and current affairs television channel."
        }
    },
    "India": {
        "WION": {
            "id": "UC_gUM8rL-Lrg6O3adPWZwqQ",
            "country": "India",
            "category": "World News",
            "desc": "World Is One News - international news with South Asian perspective."
        },
        "India Today": {
            "id": "UCYPvAwZP8pZhSMW8qsG1X3w",
            "country": "India",
            "category": "National & World",
            "desc": "India's premier English news channel."
        },
        "NDTV": {
            "id": "UCZFMm1mMw0F81Z37aaEzTUA",
            "country": "India",
            "category": "National & World",
            "desc": "Credible, comprehensive Indian and world news."
        },
        "Aaj Tak": {
            "id": "UCt4t-jeY85JegMlZ-E5UWtA",
            "country": "India",
            "category": "National Hindi",
            "desc": "India's leading Hindi news channel."
        },
        "Republic World": {
            "id": "UCwvdTZK-B1F8U9t83Y6aokg",
            "country": "India",
            "category": "National & Debate",
            "desc": "Breaking news, debates, and national stories."
        },
        "CNN-News18": {
            "id": "UC9C37L5A0UImD1_xIeJ3XWw",
            "country": "India",
            "category": "National English",
            "desc": "Partnership news broadcaster in India."
        },
        "Times Now": {
            "id": "UC6rj7-44qQL6CX322WpxVMA",
            "country": "India",
            "category": "National English",
            "desc": "Action-oriented Indian news television channel."
        },
        "DD India": {
            "id": "UCv9GZ11v_t7Xl0_r9Y6_bLg",
            "country": "India",
            "category": "Public Broadcaster",
            "desc": "India's international news and public broadcast service."
        }
    },
    "Asia Pacific": {
        "CNA (Singapore)": {
            "id": "UC83jt4dlz1Gjl58fzQrrKZg",
            "country": "Singapore",
            "category": "Asia News",
            "desc": "Channel NewsAsia - in-depth coverage of Asian affairs and world news."
        },
        "South China Morning Post": {
            "id": "UC4SUWjzWg5_jWQjX5-D-qJw",
            "country": "Hong Kong",
            "category": "China & Asia",
            "desc": "Authoritative news reporting on China and Asia."
        },
        "CGTN (China)": {
            "id": "UCgrNz-aDmcr2uuto8_DL2jg",
            "country": "China",
            "category": "International",
            "desc": "China Global Television Network - international news."
        },
        "NHK WORLD-JAPAN": {
            "id": "UCSPEjw8F2nQDtmUKPFNF7_A",
            "country": "Japan",
            "category": "Asia & Japan",
            "desc": "Japan's international broadcasting service."
        },
        "Arirang News (South Korea)": {
            "id": "UCUeJXhGrsLr_OQ8sIu4N5Ow",
            "country": "South Korea",
            "category": "Korea & World",
            "desc": "English-language broadcaster based in Seoul, South Korea."
        },
        "KBS WORLD TV (South Korea)": {
            "id": "UC5BMQOsAB8hKUyHu9KI6yig",
            "country": "South Korea",
            "category": "Korea & Culture",
            "desc": "Korean Broadcasting System international channel."
        },
        "TaiwanPlus News": {
            "id": "UCe_lG3eK7G5K9y5B1X9m5zg",
            "country": "Taiwan",
            "category": "Taiwan & Asia",
            "desc": "Taiwan's first English-language global news and video platform."
        }
    },
    "Australia & Canada": {
        "ABC News Australia": {
            "id": "UCe1FWti-C2A8Y2kYt-r5RcA",
            "country": "Australia",
            "category": "Public Broadcaster",
            "desc": "Australian Broadcasting Corporation 24/7 continuous news."
        },
        "Sky News Australia": {
            "id": "UCO0akEElkWrbFC30n-K0VHQ",
            "country": "Australia",
            "category": "National & Opinion",
            "desc": "Australian 24-hour cable and satellite news channel."
        },
        "9 News Australia": {
            "id": "UCWq4r3P3oH0o2_oX9t7rEew",
            "country": "Australia",
            "category": "National News",
            "desc": "Nine Network's national news service."
        },
        "7NEWS Australia": {
            "id": "UCj4b9t_E8oN634NqZqH1m-A",
            "country": "Australia",
            "category": "National News",
            "desc": "Seven Network's television news service."
        },
        "CBC News (Canada)": {
            "id": "UCuVcGjOENzK2v28YtcT0gQA",
            "country": "Canada",
            "category": "Public Broadcaster",
            "desc": "Canadian Broadcasting Corporation live and investigative news."
        },
        "Global News (Canada)": {
            "id": "UChLtXXbpSYDIGV9VidD-3aw",
            "country": "Canada",
            "category": "National News",
            "desc": "Canadian news, breaking alerts, and in-depth video features."
        },
        "CTV News (Canada)": {
            "id": "UCY0C8wH5q-u_n4J2o6B2A8A",
            "country": "Canada",
            "category": "National News",
            "desc": "Canada's largest private broadcaster."
        }
    }
}

# Master flat list of all channels
ALL_CHANNELS = {}
for region, channels in CHANNELS_BY_REGION.items():
    for name, data in channels.items():
        entry = dict(data)
        entry["region"] = region
        ALL_CHANNELS[name] = entry

# Mapping of NewsHub regions to Google News RSS parameters
REGION_TO_GOOGLE_NEWS = {
    "All": {"hl": "en-US", "gl": "US", "ceid": "US:en"},
    "United States": {"hl": "en-US", "gl": "US", "ceid": "US:en"},
    "United Kingdom": {"hl": "en-GB", "gl": "GB", "ceid": "GB:en"},
    "Europe": {"query": "Europe news headlines"},
    "Middle East & Africa": {"query": "Middle East Africa news headlines"},
    "India": {"hl": "en-IN", "gl": "IN", "ceid": "IN:en"},
    "Asia Pacific": {"query": "Asia Pacific international news"},
    "Australia & Canada": {"hl": "en-AU", "gl": "AU", "ceid": "AU:en"}
}

# Standard Google News topic categories
GOOGLE_NEWS_TOPICS = {
    "🔥 Top Stories": None,
    "🌐 World": "WORLD",
    "💼 Business": "BUSINESS",
    "💻 Technology & AI": "TECHNOLOGY",
    "🔬 Science & Space": "SCIENCE",
    "🏥 Health": "HEALTH",
    "🎬 Entertainment": "ENTERTAINMENT",
    "⚽ Sports": "SPORTS"
}
