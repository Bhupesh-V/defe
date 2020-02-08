import urllib.request
import json


def get(url: str, params=None):
    """Request URL"""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        req = response.read()

    data = json.loads(req.decode("utf-8"))

    return data
