#!/usr/bin/python3
""" nuumber of subs in a subreddit """
import requests


def number_of_subscribers(subreddit):
    """ return number of subs in subreddit """
    h = {'User-Agent': 'reddit_user'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    rq = requests.get(url, headers=h, allow_redirects=False)
    if rq.status_code == 200:
        return (rq.json().get("data").get("subscribers"))
    return 0
