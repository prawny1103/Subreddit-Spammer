import praw
import time

username = input("Reddit username: ")
password = input("Reddit password: ")
title = input("Post title: ")
url = "https://preview.redd.it/omfop10766161.png?width=360&format=png&auto=webp&s=72680f8da7d957347720d1277495068d72b1d6b5"

reddit = praw.Reddit(client_id='aPSsYrc-eTTh8Q',
                     client_secret='vf68ATEDQ9SEfGGEEoHZyf2FC4TAvg',
                     username=username,
                     password=password,
                     user_agent='user agent'
                     )
reddit.validate_on_submit = True

subreddit = reddit.subreddit("GlobalSteamTrade")

while True:
    subreddit.submit(title=title, url=url)
    time.sleep(3)
