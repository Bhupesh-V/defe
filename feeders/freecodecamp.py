import feedparser

url = "https://www.freecodecamp.org/news/rss/"
freecodecamp_feed = feedparser.parse(url)


def feed():
    return freecodecamp_feed.entries
