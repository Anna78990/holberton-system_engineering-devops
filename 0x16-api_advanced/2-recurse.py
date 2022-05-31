#!/usr/bin/python3
"""returns the title lists"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """returns the title lists"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    p = {"after": after}
    res = requests.get(url, headers={'User-agent': 'your bot 0.1'}, params=p)
    if res.status_code == 404:
        return None
    after = res.json().get("data").get("after")
    for re in res.json().get("data").get("children"):
        hot_list.append(re.get("data").get("title"))
    if after is not None:
        """ else return oht_list ne fonctionne pas"""
        recurse(subreddit, hot_list, after)
        return hot_list
