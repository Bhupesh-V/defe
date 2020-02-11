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

sort = [
    "hot",
    "top",
    "new",
    "rising"
]


def subreddit(sub, sort_by):
    if sub in subreddits and sort_by in sort:
        url = f"https://www.reddit.com/r/{sub}/{sort_by}.rss"
        feed = feedparser.parse(url)

        return feed.entries
    else:
        return {"error": "Subreddit Not Available"}
