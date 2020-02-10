import urllib.request
import json

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}


def get(url: str, params=None):
    """Request URL"""
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as response:
        req = response.read()

    data = json.loads(req.decode("utf-8"))

    return data
