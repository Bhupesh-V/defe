from modules.request import get

# HackerNews Feed

# TODO:
# 1. Use async feature to render each unique story

API_URL = "https://hacker-news.firebaseio.com/v0"


def get_item(item: str):
    story = get(f'{API_URL}/item/{item}.json?print=pretty')
    # https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty

    return story


def get_top():
    """Get Top stories"""
    top_stories = get(API_URL + "/topstories.json?print=pretty")

    top_stories = [get_item(story) for story in top_stories]

    print(top_stories)

    return top_stories


def get_new():
    """Get New stories"""
    new_stories = get(API_URL + "/newstories.json?print=pretty")

    return new_stories


def get_ask():
    """Get Ask stories"""
    ask_stories = get(API_URL + "/askstories.json?print=pretty")

    return ask_stories
