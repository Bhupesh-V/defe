import feedparser

url = "https://www.producthunt.com/feed"
feed = feedparser.parse(url)


def producthunt():
    return feed.entries
