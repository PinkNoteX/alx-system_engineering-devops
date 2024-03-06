#!/usr/bin/python3
""" return number of subs in subreddit """
import requests


def number_of_subscribers(subreddit):
    """ return number of subs in subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alx_0x16_api_advanced"}
    rq = requests.get(url, headers=headers, allow_redirects=False)
    if rq.status_code == 200:
        data = rq.json()
        subs = data['data']['subscribers']
        return subs
    else:
        return 0
