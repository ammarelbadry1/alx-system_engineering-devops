#!/usr/bin/python3
"""This module contains a function that queries the Reddit API
and returns the number of subscribers for a given subreddit."""
import requests
import pprint


def number_of_subscribers(subreddit):
    """Queries the Reddit API for a given subreddit"""

    url = "https://www.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "Chrome/122.0"}

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return 0

    res_obj = r.json()

    if 'data' not in res_obj:
        return 1
    if 'subscribers' not in res_obj.get('data'):
        return 2

    return res.json()["data"]["subscribers"]
