import feedparser

url = "https://techcrunch.com/feed/"
d = feedparser.parse(url)


def techcrunch():
    return d.entries
