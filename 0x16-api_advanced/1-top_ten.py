#!/usr/bin/python3
""" print top posts of subreddit """
import requests


def top_ten(subreddit):
    """ return top 10 posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "reddit_user"}
    params = {"limit": 10}
    rq = requests.get(url, headers=headers, params=params, allow_redirects=True)
    if rq.status_code != 200:
        print(rq.status_code)
        return
    else:
        res = rq.json().get("data")
        [print(x.get("title")) for x in res.get("children")]
