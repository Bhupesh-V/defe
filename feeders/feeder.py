import feedparser
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
import itertools
import random
import json
import os
from tqdm import tqdm


def read_data(feed_type=None):
    if feed_type == "podcast":
        podcast_file = os.path.join(os.getcwd(), "feeders/static", "podcasts.json")
        with open(podcast_file) as json_file:
            data = json.load(json_file)
        return data["podcasts"]
    elif feed_type == "news":
        news_file = os.path.join(os.getcwd(), "feeders/static", "news.json")
        with open(news_file) as json_file:
            data = json.load(json_file)
        return data["news"]
    elif feed_type == "general":
        general_file = os.path.join(os.getcwd(), "feeders/static", "general.json")
        with open(general_file) as json_file:
            data = json.load(json_file)
        return data["general"]
    elif feed_type == "newsletter":
        newsletter_file = os.path.join(os.getcwd(), "feeders/static", "newsletters.json")
        with open(newsletter_file) as json_file:
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
    podcasts = read_data("podcast")
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(tqdm(executor.map(get_latest_feed, [key["link"] for key in podcasts]), total=len(podcasts)))

    return results


def newsletters_feeds():
    newsletters = read_data("newsletter")
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(tqdm(executor.map(get_latest_feed, [key["link"] for key in newsletters]), total=len(newsletters)))

    return results


def news_feed():
    news = read_data("news")
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(tqdm(executor.map(get_feed, [key["link"] for key in news]), total=len(news)))

    feed_result = [i for i in itertools.chain.from_iterable(results)]

    random.shuffle(feed_result)

    for f in feed_result:
        f["feeder_site"] = get_domain(f["link"])

    return feed_result


# def feed(feeder_site: str):
#     if feeder_site in feeder_site_urls:
#         return get_feed(feeder_site_urls[feeder_site])
#     else:
#         return {"error": "Feeder Site Not Available"}


def all_feed():
    general = read_data("general")
    with ThreadPoolExecutor(max_workers=30) as executor:
        results = list(tqdm(executor.map(get_feed, [key["link"] for key in general]), total=len(general)))

    feed_result = [i for i in itertools.chain.from_iterable(results)]

    random.shuffle(feed_result)

    for f in feed_result:
        f["feeder_site"] = get_domain(f["link"])

    return feed_result
