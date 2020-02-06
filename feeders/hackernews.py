from modules.request import get

# HackerNews Feed

# TODO:
# 1. Use async feature to render each unique story

API_URL = "https://hacker-news.firebaseio.com/v0"


def get_item():
    pass


def get_top():
    """Get Top stories"""
    top_stories = get(API_URL + "/topstories.json?print=pretty")

    return top_stories


def get_new():
    """Get New stories"""
    new_stories = get(API_URL + "/newstories.json?print=pretty")

    return new_stories


def get_ask():
    """Get Ask stories"""
    ask_stories = get(API_URL + "/newstories.json?print=pretty")

    return ask_stories
