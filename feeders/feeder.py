import feedparser
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
import itertools
import random
import json
import os
feeder_site_urls = {
    "HackerNoon": "https://hackernoon.com/feed",
    "Producthunt": "https://www.producthunt.com/feed",
    "freeCodeCsamp": "https://www.freecodecamp.org/news/rss/",
    "opensource": "https://opensource.com/feed",
    "changelog": "https://changelog.com/feed",
    "itsfoss": "https://itsfoss.com/category/news/feed",
    "thenewstack": "https://thenewstack.io/feed",
    "theverge": "https://www.theverge.com/tech/rss/index.xml",
    "dev.to": "https://dev.to/feed",
    "CSS Tricks": "https://css-tricks.com/feed/",
}

news_feed_sites = {
    "TechCrunch": "https://techcrunch.com/feed/",
    "HackerNews": "https://news.ycombinator.com/rss",
    "Tech meme": "https://www.techmeme.com/feed.xml",
    "GeekWire": "https://www.geekwire.com/feed/",
    "Technology Org": "https://www.technology.org/feed/",
    "Geek.com": "https://www.geek.com/tech/feed/",
    "ZDNet": "https://www.zdnet.com/rss.xml",
    "MIT Technology Review": "https://www.technologyreview.com/topnews.rss",
    "Gigabit Magazine": "https://www.gigabitmagazine.com/rss.xml",
    "Technology Intelligence": "https://www.telegraph.co.uk/technology/rss.xml",
}


def read_data(feed_type=None):
    if feed_type == "podcasts":
        podcast_file = os.path.join(os.getcwd(), "feeders/static", "podcasts.json")
        with open(podcast_file) as json_file:
            data = json.load(json_file)
        return data["podcasts"]
    elif feed_type == "newsletter":
        newsletter_file = os.path.join(os.getcwd(), "feeders/static", "newsletters.json")
        with open(podcast_file) as json_file:
            data = json.load(json_file)
        return data["newsletters"]


def get_feed(url):
    site_feed = feedparser.parse(url)
    return site_feed.entries


def get_latest_feed(url):
    site_feed = feedparser.parse(url)
    return site_feed.entries[0]


def get_domain(link):
    domain = urlparse(link).netloc

    return domain


def podcasts_feeds():
    podcasts = read_data("podcasts")
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(get_latest_feed, [key["link"] for key in podcasts]))

    return results


def newsletters_feeds():
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(get_latest_feed, newsletters.values()))

    return results


def news():
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(get_feed, news_feed_sites.values()))

    feed_result = [i for i in itertools.chain.from_iterable(results)]

    random.shuffle(feed_result)

    for f in feed_result:
        f["feeder_site"] = get_domain(f["link"])

    return feed_result


def feed(feeder_site: str):
    if feeder_site in feeder_site_urls:
        return get_feed(feeder_site_urls[feeder_site])
    else:
        return {"error": "Feeder Site Not Available"}


def all_feed():
    with ThreadPoolExecutor(max_workers=30) as executor:
        results = list(executor.map(get_feed, feeder_site_urls.values()))

    feed_result = [i for i in itertools.chain.from_iterable(results)]

    random.shuffle(feed_result)

    for f in feed_result:
        f["feeder_site"] = get_domain(f["link"])

    return feed_result
