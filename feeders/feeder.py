import feedparser
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
from . import hackernews, devto
import itertools
import random

feeder_site_urls = {
    "hackernoon": "https://hackernoon.com/feed",
    "producthunt": "https://www.producthunt.com/feed",
    "techcrunch": "https://techcrunch.com/feed/",
    "freecodecamp": "https://www.freecodecamp.org/news/rss/",
    "opensource": "https://opensource.com/feed",
    "changelog": "https://changelog.com/feed",
    "itsfoss": "https://itsfoss.com/category/news/feed",
    "thenewstack": "https://thenewstack.io/feed",
    "theverge": "https://www.theverge.com/tech/rss/index.xml"
}


def get_feed(url):
    site_feed = feedparser.parse(url)
    return site_feed.entries


def get_domain(link):
    domain = urlparse(link).netloc

    return domain


def feed(feeder_site: str):
    if feeder_site in feeder_site_urls:
        return get_feed(feeder_site_urls[feeder_site])
    elif feeder_site == "hackernews":
        return hackernews.get_top()
    elif feeder_site == "dev.to":
        return devto.get_articles()
    else:
        return {"error": "Feeder Site Not Available"}


def all_feed():
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(get_feed, feeder_site_urls.values()))

    feed_result = [i for i in itertools.chain.from_iterable(results)]

    random.shuffle(feed_result)

    for f in feed_result:
        f["feeder_site"] = get_domain(f["link"])

    return feed_result
