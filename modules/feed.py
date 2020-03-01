from diskcache import Cache
import feedparser


def __manage_cache(url: str):
    cache = Cache(".feedcache")
    try:
        if url in cache:
            data = cache.get(url)
        else:
            parsed_feed = feedparser.parse(url)
            data = parsed_feed
            cache.add(url, parsed_feed, expire=3600)
        cache.close()
    except ValueError:
        pass
    return data


def get_feed(url: str):
    return __manage_cache(url).entries


def get_latest_feed(url: str):
    return __manage_cache(url).entries[0]
