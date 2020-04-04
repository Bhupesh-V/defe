import feedparser
from diskcache import Cache


class cache:
    def __init__(self, latest=False):
        self.feedCache = Cache(".feedcache")
        self.latest = latest

    def __preprocess_title(self, feed):
        for entry in feed.entries:
            entry["feed_src"] = feed["feed"]["title"]

        return feed

    def __manage_cache(self, url):
        try:
            if url in self.feedCache:
                data = self.feedCache.get(url)
            else:
                parsed_feed = feedparser.parse(url)
                data = self.__preprocess_title(parsed_feed)
                # cache expires in 30 mins
                self.feedCache.add(url, data, expire=1800)
            self.feedCache.close()
        except ValueError:
            pass
        except Exception:
            pass
        return data

    def get_feed(self, url):
        if self.latest:
            latestFeed = self.__manage_cache(url).entries
            if len(latestFeed) > 0:
                return latestFeed[0]
            else:
                pass

        return self.__manage_cache(url).entries
