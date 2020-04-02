import itertools
import json
import os
import random
from concurrent.futures import ThreadPoolExecutor

from tqdm import tqdm

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


try:
    from core.feed import cache
except ModuleNotFoundError:
    from defe.core.feed import cache


def read_data(feed_type=None):
    if feed_type == "podcasts":
        podcast_file = os.path.join(
            os.path.dirname(__file__), "feeders", "podcasts.json"
        )
        with open(podcast_file) as json_file:
            data = json.load(json_file)
        return data["podcasts"]
    elif feed_type == "news":
        news_file = os.path.join(os.path.dirname(__file__), "feeders", "news.json")
        with open(news_file) as json_file:
            data = json.load(json_file)
        return data["news"]
    elif feed_type == "general":
        general_file = os.path.join(
            os.path.dirname(__file__), "feeders", "general.json"
        )
        with open(general_file) as json_file:
            data = json.load(json_file)
        return data["general"]
    elif feed_type == "newsletters":
        newsletter_file = os.path.join(
            os.path.dirname(__file__), "feeders", "newsletters.json"
        )
        with open(newsletter_file) as json_file:
            data = json.load(json_file)
        return data["newsletters"]


def get_domain(link):
    domain = urlparse(link).netloc

    return domain


def fetcher(category, latest=False, show_progress=False, workers=27):
    data = read_data(category)
    feeddata = cache()
    with ThreadPoolExecutor(max_workers=workers) as executor:
        if latest:
            results = list(
                tqdm(
                    executor.map(
                        feeddata.get_latest_feed, [key["link"] for key in data]
                    ),
                    desc="Fetching Feeders",
                    total=len(data),
                    disable=show_progress,
                    leave=False,
                )
            )
        else:
            results = list(
                tqdm(
                    executor.map(feeddata.get_feed, [key["link"] for key in data]),
                    desc="Fetching Feeders",
                    total=len(data),
                    disable=show_progress,
                    leave=False,
                )
            )

    return results


def podcasts_feeds(show_progress=False, workers=27):
    result = fetcher("podcasts", True, show_progress, workers)

    return result


def newsletters_feeds(show_progress=False, workers=30):
    result = fetcher("newsletters", True, show_progress, workers)

    return result


def news_feed(show_progress=False, workers=20):
    result = fetcher("news", False, show_progress, workers)

    feed_result = [i for i in itertools.chain.from_iterable(result)]

    random.shuffle(feed_result)

    for f in feed_result:
        f["feeder_site"] = get_domain(f["link"])

    return feed_result


def feed(feeder_site_url):
    feeddata = cache()
    return feeddata.get_feed(feeder_site_url)


def all_feed(show_progress=False, workers=20):
    result = fetcher("general", False, show_progress, workers)

    feed_result = [i for i in itertools.chain.from_iterable(result)]

    random.shuffle(feed_result)

    for f in feed_result:
        f["feeder_site"] = get_domain(f["link"])

    return feed_result
