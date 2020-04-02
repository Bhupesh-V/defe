import feedparser
from diskcache import Cache


class cache:
    def __init__(self):
        self.feedCache = Cache(".feedcache")

    def __manage_cache(self, url):
        try:
            if url in self.feedCache:
                data = self.feedCache.get(url)
            else:
                parsed_feed = feedparser.parse(url)
                data = parsed_feed
                # cache expires in 1hr
                self.feedCache.add(url, parsed_feed, expire=1800)
            self.feedCache.close()
        except ValueError:
            pass
        except Exception as e:
            pass
        return data

    def get_feed(self, url):
        return self.__manage_cache(url).entries

    def get_latest_feed(self, url):
        latestFeed = self.__manage_cache(url).entries
        if len(latestFeed) > 0:
            return latestFeed[0]
        else:
            pass
