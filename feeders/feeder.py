import feedparser
from concurrent.futures import ThreadPoolExecutor

feeder_site_urls = {
    "hackernoon": "https://hackernoon.com/feed",
    "producthunt": "https://www.producthunt.com/feed",
    "techcrunch": "https://techcrunch.com/feed/",
    "freecodecamp": "https://www.freecodecamp.org/news/rss/",
    "opensource": "https://opensource.com/feed",
    "changelog": "https://changelog.com/feed",
    "itsfoss": "https://itsfoss.com/category/news/feed"
}


def get_feed(url):
    site_feed = feedparser.parse(url)
    return site_feed.entries


def feed(feeder_site: str):
    if feeder_site in feeder_site_urls:
        return get_feed(feeder_site_urls[feeder_site])
    else:
        return {"error": "Feeder Site Not Available"}


def all_feed():
    with ThreadPoolExecutor(max_workers=7) as executor:
        results = list(executor.map(get_feed, feeder_site_urls.values()))

    return results
