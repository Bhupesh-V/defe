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
    if feed_type in ["podcasts", "news", "general", "newsletters"]:
        feeders = os.path.join(
            os.path.dirname(__file__), "feeders", feed_type + ".json"
        )
        with open(feeders) as json_file:
            data = json.load(json_file)
        return data[feed_type]
    return None

def get_header_image(item):
    try:
        if len(item['links']) > 1:
            link_type = item['links'][1]['type']

            if (link_type == 'image/png' or link_type == 'image/jpeg'):
                return item['links'][1]['href']
    except:
        # no image link found
        pass


def get_domain(link):
    domain = urlparse(link).netloc

    return domain


def fetcher(category, latest=False, show_progress=False, workers=27):
    data = read_data(category)
    feeddata = cache(latest)
    with ThreadPoolExecutor(max_workers=workers) as executor:
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

def filter_mpeg_link(result):
    for item in result:
        # filter only mp3 links
        item["links"] = [link for link in item["links"] if link["type"] == "audio/mpeg"]
        if len(item["links"]) < 1:
            result.remove(item)

    return result

def podcasts_feeds(show_progress=False, workers=27):
    result = fetcher("podcasts", True, show_progress, workers)

    return filter_mpeg_link(result)


def newsletters_feeds(show_progress=False, workers=30):
    result = fetcher("newsletters", True, show_progress, workers)

    return result


def news_feed(show_progress=False, workers=20):
    result = fetcher("news", False, show_progress, workers)

    feed_result = [i for i in itertools.chain.from_iterable(result)]

    random.shuffle(feed_result)

    for f in feed_result:
        f["feeder_site"] = get_domain(f["link"])
        f["image"] = get_header_image(f)

    return feed_result


def feed(feeder_site_url):
    # feed for a single feeder source
    feeddata = cache()
    return feeddata.get_feed(feeder_site_url)


def all_feed(show_progress=False, workers=20):
    result = fetcher("general", False, show_progress, workers)

    feed_result = [i for i in itertools.chain.from_iterable(result)]

    random.shuffle(feed_result)

    for f in feed_result:
        f["feeder_site"] = get_domain(f["link"])
        f["image"] = get_header_image(f)

    return feed_result
