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
    "codenewbie": "http://feeds.codenewbie.org/cnpodcast.xml",
    "codingblocks": "https://www.codingblocks.net/feed/podcast/",
    "coderradio": "https://feeds.fireside.fm/coder/rss",
    "testandcode": "https://feeds.fireside.fm/testandcode/rss",
    "stackoverflowpodcast": "https://feeds.simplecast.com/XA_851k3",
    "weeklydevtips": "https://feeds.simplecast.com/W8bGHhCA"
}

newsletters = {
    "golangweekly": "https://golangweekly.com/rss",
    "rubyweekly": "https://rubyweekly.com/rss",
    "nodeweekly": "https://nodeweekly.com/rss",
    "cssweekly": "https://feeds.feedburner.com/CSS-Weekly",
    "dbweekly": "https://dbweekly.com/rss",
    "mobiledevweekly": "https://mobiledevweekly.com/rss",
    "javascriptweekly": "https://javascriptweekly.com/rss",
    "frontendfocus": "https://frontendfoc.us/rss",
    "androidweekly": "http://us2.campaign-archive1.com/feed?u=887caf4f48db76fd91e20a06d&id=4eb677ad19",
    "pycoder": "https://pycoders.com/feed",
    "awesomeandroid": "https://android.libhunt.com/newsletter/feed",
    "awesomecpp": "https://cpp.libhunt.com/newsletter/feed",
    "awesomego": "https://go.libhunt.com/newsletter/feed",
    "awesomejs": "https://js.libhunt.com/newsletter/feed",
    "awesomepython": "https://python.libhunt.com/newsletter/feed",
    "awesomedotnet": "https://dotnet.libhunt.com/newsletter/feed",
    "awesomephp": "https://php.libhunt.com/newsletter/feed",
    "awesomerust": "https://rust.libhunt.com/newsletter/feed",
    "awesomeruby": "https://ruby.libhunt.com/newsletter/feed",
    "awesomeswift": "https://swift.libhunt.com/newsletter/feed",
    "awesomescala": "https://scala.libhunt.com/newsletter/feed",
    "awesomenodejs": "https://nodejs.libhunt.com/newsletter/feed",
    "awesomekotlin": "https://kotlin.libhunt.com/newsletter/feed",
    "awesomeelixir": "https://elixir.libhunt.com/newsletter/feed",
    "awesomeios": "https://ios.libhunt.com/newsletter/feed",
    "awesomejava": "https://java.libhunt.com/newsletter/feed",
    "awesomesysadmin": "https://sysadmin.libhunt.com/newsletter/feed",
}


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
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(get_latest_feed, podcasts.values()))

    return results


def newsletters_feeds():
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(get_latest_feed, newsletters.values()))

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
