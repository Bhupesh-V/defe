import feedparser

url = "https://hackernoon.com/feed"
hackenoon_feed = feedparser.parse(url)


def feed():
    return hackenoon_feed.entries
