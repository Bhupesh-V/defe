import feedparser
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
import itertools
import random

feeder_site_urls = {
    "HackerNoon": "https://hackernoon.com/feed",
    "Producthunt": "https://www.producthunt.com/feed",
    "TechCrunch": "https://techcrunch.com/feed/",
    "freeCodeCsamp": "https://www.freecodecamp.org/news/rss/",
    "opensource": "https://opensource.com/feed",
    "changelog": "https://changelog.com/feed",
    "itsfoss": "https://itsfoss.com/category/news/feed",
    "thenewstack": "https://thenewstack.io/feed",
    "theverge": "https://www.theverge.com/tech/rss/index.xml",
    "dev.to": "https://dev.to/feed",
    "HackerNews": "https://news.ycombinator.com/rss",
    "CSS Tricks": "https://css-tricks.com/feed/",
    "Tech meme": "https://www.techmeme.com/feed.xml"
}

podcasts = {
    "Software Enginerring Daily": "https://softwareengineeringdaily.com/feed/podcast/",
    "Simple Programmer": "http://simpleprogrammer.libsyn.com/rss",
    "Software Enginerring Radio": "http://feeds.feedburner.com/se-radio",
    "The Changelog": "https://changelog.com/podcast/feed",
    "Full Stack Radio": "https://rss.simplecast.com/podcasts/279/rss",
    "codenewbie": "http://feeds.codenewbie.org/cnpodcast.xml",
    "Coding Blocks": "https://www.codingblocks.net/feed/podcast/",
    "Coder Radio": "https://feeds.fireside.fm/coder/rss",
    "Test and Code": "https://feeds.fireside.fm/testandcode/rss",
    "Stackoverflow Podcast": "https://feeds.simplecast.com/XA_851k3",
    "Weekly Dev Tips": "https://feeds.simplecast.com/W8bGHhCA",
    "cpp.chat": "https://feeds.fireside.fm/cppchat/rss",
    "devpath.fm": "https://feeds.transistor.fm/devpath-fm",
    "synatx.fm": "feed.syntax.fm/rss",
    "Talk Python": "https://talkpython.fm/episodes/rss"
}

newsletters = {
    "Golang Weekly": "https://golangweekly.com/rss",
    "Ruby Weekly": "https://rubyweekly.com/rss",
    "Node Weekly": "https://nodeweekly.com/rss",
    "PHP Weekly": "http://www.phpweekly.com/rss.xml",
    "CSS Weekly": "https://feeds.feedburner.com/CSS-Weekly",
    "Database Weekly": "https://dbweekly.com/rss",
    "Mobile Dev Weekly": "https://mobiledevweekly.com/rss",
    "Javascript Weekly": "https://javascriptweekly.com/rss",
    "Frontend Focus": "https://frontendfoc.us/rss",
    "Postgres Weekly": "https://postgresweekly.com/rss",
    "Android Weekly": "http://us2.campaign-archive1.com/feed?u=887caf4f48db76fd91e20a06d&id=4eb677ad19",
    "PyCoder": "https://pycoders.com/feed",
    "Awesome Android": "https://android.libhunt.com/newsletter/feed",
    "Awesome C++": "https://cpp.libhunt.com/newsletter/feed",
    "Awesome Go": "https://go.libhunt.com/newsletter/feed",
    "Awesome Javascript": "https://js.libhunt.com/newsletter/feed",
    "Awesome Python": "https://python.libhunt.com/newsletter/feed",
    "Awesome .NET": "https://dotnet.libhunt.com/newsletter/feed",
    "Awesome php": "https://php.libhunt.com/newsletter/feed",
    "Awesome Rust": "https://rust.libhunt.com/newsletter/feed",
    "Awesome Ruby": "https://ruby.libhunt.com/newsletter/feed",
    "Awesome Swift": "https://swift.libhunt.com/newsletter/feed",
    "Awesome Scala": "https://scala.libhunt.com/newsletter/feed",
    "Awesome Nodejs": "https://nodejs.libhunt.com/newsletter/feed",
    "Awesome Kotlin": "https://kotlin.libhunt.com/newsletter/feed",
    "Awesome Elixir": "https://elixir.libhunt.com/newsletter/feed",
    "Awesome iOS": "https://ios.libhunt.com/newsletter/feed",
    "Awesome Java": "https://java.libhunt.com/newsletter/feed",
    "Awesome Awesomesysadmin": "https://sysadmin.libhunt.com/newsletter/feed",
    "Web Development Reading List (WDRL)": "https://wdrl.info/feed",
    "Pony Foo Weekly": "https://feeds.feedburner.com/ponyfooweekly",
    "R Weekly": "https://rweekly.org/atom.xml",
    "mongoDB Memo": "https://mongodb.email/rss",
    "Azure Weekly": "https://azureweekly.info/rss.xml",
    "Serverless Status": "https://serverless.email/rss",
    "Last Week in AWS": "https://www.lastweekinaws.com/newsletter/feed",
    "artificial intelligence digest": "https://feeds.feedburner.com/digest-ai",
    "Inside AI": "https://inside.com/ai/rss",
    "TLDR": "https://www.tldrnewsletter.com/rss",
    "Barista Tech News": "https://www.barista.io/feeds/tech/latest.rss"
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
