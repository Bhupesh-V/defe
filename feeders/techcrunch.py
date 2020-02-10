import feedparser

url = "https://techcrunch.com/feed/"
techcrunch_feed = feedparser.parse(url)


def feed():
    return techcrunch_feed.entries
