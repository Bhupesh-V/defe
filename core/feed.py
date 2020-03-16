from diskcache import Cache
import feedparser


def __manage_cache(url):
    cache = Cache(".feedcache")
    try:
        if url in cache:
            data = cache.get(url)
        else:
            parsed_feed = feedparser.parse(url)
            data = parsed_feed
            cache.add(url, parsed_feed, expire=1800)
        cache.close()
    except ValueError:
        pass
    except Exception as e:
        pass
    return data


def get_feed(url):
    return __manage_cache(url).entries


def get_latest_feed(url):
    return __manage_cache(url).entries[0]
