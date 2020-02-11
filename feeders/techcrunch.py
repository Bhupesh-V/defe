import feedparser

url = "https://techcrunch.com/feed/"
techcrunch_feed = feedparser.parse(url)


def feed():
    print(techcrunch_feed)
    return techcrunch_feed.entries
