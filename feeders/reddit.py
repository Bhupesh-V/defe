import feedparser

subreddits = [
    "programming",
    "technology",
    "cpp",
    "python",
    "javascript",
]


def subreddit(sub):
    if sub in subreddits:
        url = f'https://www.reddit.com/r/{sub}/new.rss'
        feed = feedparser.parse(url)

        return feed.entries
    else:
        return {"error": "Subreddit Not Available"}
