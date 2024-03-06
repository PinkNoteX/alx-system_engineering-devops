#!/usr/bin/python3
""" get number of subs in subreddit """
import requests


def number_of_subscribers(subreddit):
    """ get number of subs """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'subreddit-counter'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    try:
        d = res.json().get("data")
        return d.get("subscribers")
    except ValueError:
        return 0
