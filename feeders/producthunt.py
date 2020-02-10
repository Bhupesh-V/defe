import feedparser

url = "https://www.producthunt.com/feed"
producthunt_feed = feedparser.parse(url)


def feed():
    return producthunt_feed.entries
