#!/usr/bin/python3
""" print top posts of subreddit """
import requests


def top_ten(subreddit):
    """ return top 10 posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "alx_0x16_api_advanced"}
    lm = {"limit": 10}
    rq = requests.get(url, headers=headers, params=lm, allow_redirects=False)
    if rq.status_code == 404:
        print("None")
        return
    else:
        res = rq.json().get("data")
        [print(x.get("title")) for x in res.get("children")]
