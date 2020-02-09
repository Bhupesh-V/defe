import feedparser

subreddits = [
    "programming",
    "technology",
    "cpp",
    "python",
    "javascript",
    "Android",
    "learnprogramming",
    "software",
    "startups",
    "tech",
    "web_design",
    "linux",
    "computing",
    "coding",
    "AskTechnology",
    "webdev"
]


def subreddit(sub):
    if sub in subreddits:
        url = f"https://www.reddit.com/r/{sub}/new.rss"
        feed = feedparser.parse(url)

        return feed.entries
    else:
        return {"error": "Subreddit Not Available"}
