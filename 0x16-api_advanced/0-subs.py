#!/usr/bin/python3
"""returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    res = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    if res.status_code > 300:
        return res.status_code

    return res.json().get("data").get("subscribers")
