"""defe package."""

try:
    from defe.core import feedcore
except ImportError:
    from core import feedcore


class NoSuchFeederCategory(Exception):

    """Custom Exception for Invalid feeder."""


class feed:
    def __init__(self, progress=True):
        """Args
        - progress
        - workers
        """
        self.show_progress = progress
        self.feeder_categories = ["general", "news", "podcasts", "newsletters"]

    def feed_site(self, url):
        if url is not None:
            return feedcore.feed(url)

    def newsletters(self):
        data = feedcore.newsletters_feeds(self.show_progress)

        return data

    def news(self):
        data = feedcore.news_feed(self.show_progress)

        return data

    def general(self):
        data = feedcore.all_feed(self.show_progress)

        return data

    def podcasts(self):
        data = feedcore.podcasts_feeds(self.show_progress)

        return data

    def feeders(self, feeder):
        if feeder not in self.feeder_categories:
            raise NoSuchFeederCategory
        else:
            return feedcore.read_data(feeder)
