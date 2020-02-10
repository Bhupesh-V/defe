from modules.request import get
from concurrent.futures import ThreadPoolExecutor

# HackerNews Feed


API_URL = "https://hacker-news.firebaseio.com/v0"


def get_item(item: str):
    story = get(f"{API_URL}/item/{item}.json?print=pretty")

    return story


def get_top():
    """Get Top stories"""
    top_stories = get(API_URL + "/topstories.json?print=pretty")

    with ThreadPoolExecutor(max_workers=30) as executor:
        results = list(executor.map(get_item, top_stories[:50]))

    return results


def get_new():
    """Get New stories"""
    new_stories = get(API_URL + "/newstories.json?print=pretty")
    with ThreadPoolExecutor(max_workers=40) as executor:
        results = list(executor.map(get_item, new_stories[:50]))

    return results


def get_ask():
    """Get Ask stories"""
    ask_stories = get(API_URL + "/askstories.json?print=pretty")
    with ThreadPoolExecutor(max_workers=40) as executor:
        results = list(executor.map(get_item, ask_stories[:50]))

    return results
