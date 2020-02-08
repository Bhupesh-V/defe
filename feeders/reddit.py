import os
import praw

from dotenv import load_dotenv
load_dotenv()

client_id = os.getenv("CLIENT_ID")
secret = os.getenv("SECRET")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
reddit = praw.Reddit(client_id=client_id,
                     client_secret=secret,
                     user_agent='defe',
                     username=username,
                     password=password)


subreddit = reddit.subreddit('programming')
new_subreddit = subreddit.new(limit=30)

for d in new_subreddit:
    print(d.title, d.score, d.url)

"""
Subreddits to-do
1. https://www.reddit.com/r/technology/
2. https://www.reddit.com/r/reverseengineering/
3. https://www.reddit.com/r/learnprogramming
4. https://www.reddit.com/r/cscareerquestions
5. https://www.reddit.com/r/webdev

"""
