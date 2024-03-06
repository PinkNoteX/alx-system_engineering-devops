#!/usr/bin/python3
""" print top posts of subreddit """
import requests


def top_ten(subreddit):
    """ return top 10 posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "python:alx_0x16_api_advanced:v0.1"}
    lm = {"limit": 10}
    rq = requests.get(url, headers=headers, params=lm, allow_redirects=True)
    if rq.status_code != 200:
        print("None")
        return
    else:
        res = rq.json().get("data")
        [print(x.get("title")) for x in res.get("children")]
