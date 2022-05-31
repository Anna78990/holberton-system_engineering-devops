#!/usr/bin/python3
"""print the titles"""
import requests


def top_ten(subreddit):
    """print the titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    res = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    if res.status_code > 300:
        print("None")
        return
    data = res.json().get("data")
    for i in range(0, 10):
        print(data.get("children")[i].get("data").get("title"))
