#!/usr/bin/env python3

from secrets import *
import tweepy
import glob

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

import os
import datetime

os.chdir("content/terminology")
terms = glob.glob("*md")
week = datetime.date(2010, 6, 16).isocalendar()[1]
term = (terms[week % len(terms)])
term = term.replace(".md", "")
link = "https://www.zerotoasiccourse.com/terminology/%s" % term
twitter_text = "#ASIC terminology of the week!\n\n%s" % link

print(twitter_text)


try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")


api.update_status(status = twitter_text)

