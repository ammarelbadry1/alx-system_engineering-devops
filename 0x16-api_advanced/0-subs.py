#!/usr/bin/python3
"""This module contains a function that queries the Reddit API
and returns the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API for a given subreddit"""

    url = "https://www.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "Chrome/122.0"}

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return 0

    res_obj = r.json()

    return res_obj.get("data").get("subscribers")
