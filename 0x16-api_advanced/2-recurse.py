#!/usr/bin/python3
"""This module contains a function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given
subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries Reddit API for all hot articles for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot".format(subreddit)
    headers = {"User-Agent": "Chrome/122.0"}
    payload = {"after": after}

    r = requests.get(url, headers=headers, params=payload,
                     allow_redirects=False)

    if r.status_code != 200:
        return None

    res_obj = r.json()
    posts = res_obj["data"]["children"]
    for post in posts:
        hot_list.append(post["data"]["title"])
    after = res_obj["data"]["after"]

    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
