from modules.request import get


API_URL = "https://dev.to/api"


def get_articles():
    articles = get(API_URL + "/articles")

    return articles
