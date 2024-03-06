#!/usr/bin/python3
"""This module contains a function that queries the Reddit API, parses
the title of all hot articles, and prints a sorted count of given
keywords."""
import requests


def count_words(subreddit, word_list, after=None):
    """Queries the Reddit API for all the hot articles then prints a
    sorted count of given keywords."""

    url = "https://www.reddit.com/r/{}/hot".format(subreddit)
    headers = {"User-Agent": "Chrome/122.0"}
    payload = {"after": after}

    r = requests.get(url, headers=headers, params=payload,
                     allowed_redirects=False)

    if r.status_code != 200:
        return None

    res_obj = r.json()
    posts = res_obj["data"]["children"]
    for post in posts:
        word_list.append(post["data"]["title"])
    after = res_obj["data"]["after"]

    if not after:
        return word_list
    return recurse(subreddit, word_list, after=after)
