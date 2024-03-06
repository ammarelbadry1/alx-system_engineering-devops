#!/usr/bin/python3
"""This module contains a function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given
subreddit."""
import requests


def top_ten(subreddit):
    """Queries the Reddit API for the titles the first 10 hot posts."""

    url = "https://www.reddit.com/r/{}/hot".format(subreddit)
    headers = {"User-Agent": "Chrome/122.0"}
    payload = {"limit": 10}

    r = requests.get(url, headers=headers, params=payload,
                     allow_redirects=False)

    if r.status_code != 200:
        print("None")
        return

    res_obj = r.json()

    top_10_posts = res_obj["data"]["children"]

    if len(top_10_posts) == 0:
        print("None")
    else:
        for post in top_10_posts:
            print(post["data"]["title"])
