import praw
import re

reddit = praw.Reddit('pyeivl')
subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=5):
    if re.search("eBooks", submission.title) or \
       re.search("team", submission.selftext):
        print(submission.title)
        print(submission.selftext)
