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

podcasts = {
    "softwareenginerringdaily": "https://softwareengineeringdaily.com/feed/podcast/",
    "simpleprogrammer": "http://simpleprogrammer.libsyn.com/rss",
    "se-radio": "http://feeds.feedburner.com/se-radio",
    "thechangelog": "https://changelog.com/podcast/feed",
    "fullstackradio": "https://rss.simplecast.com/podcasts/279/rss",
    "codenewbie": "http://feeds.codenewbie.org/cnpodcast.xml"
}

newsletters = {
    "golangweekly": "https://golangweekly.com/rss",
    "rubyweekly": "https://rubyweekly.com/rss",
    "nodeweekly": "https://nodeweekly.com/rss",
    "cssweekly": "http://feeds.feedburner.com/CSS-Weekly?format=xml",
    "dbweekly": "https://dbweekly.com/rss",
    "mobiledevweekly": "https://mobiledevweekly.com/rss",
    "javascriptweekly": "https://javascriptweekly.com/rss",
    "frontendfocus": "https://frontendfoc.us/rss",
    "androidweekly": "http://us2.campaign-archive1.com/feed?u=887caf4f48db76fd91e20a06d&id=4eb677ad19",
    "pycoder": "https://pycoders.com/feed"
    # add all feeds from libhunt.com
}


def get_feed(url):
    site_feed = feedparser.parse(url)
    return site_feed.entries[0]


def get_domain(link):
    domain = urlparse(link).netloc

    return domain


def podcasts_feeds():
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(get_feed, podcasts.values()))

    # feed_result = [i for i in itertools.chain.from_iterable(results)]

    # random.shuffle(feed_result)

    # for f in feed_result:
    #     f["feeder_site"] = get_domain(f["link"])

    print(len(results))
    print(results[0])

    return results


def newsletters_feeds():
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(get_feed, newsletters.values()))

    # feed_result = [i for i in itertools.chain.from_iterable(results)]

    # random.shuffle(feed_result)

    # for f in feed_result:
    #     f["feeder_site"] = get_domain(f["link"])

    print(len(results))
    print(results[0])

    return results


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
