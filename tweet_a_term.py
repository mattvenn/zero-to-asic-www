#!/usr/bin/env python3

from secrets import *
import tweepy
import glob
from num2words import num2words

from analytics import run_report

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


import os
import datetime

analytics = run_report(property_id)

os.chdir("content/terminology")
terms = glob.glob("*md")
week = datetime.date(2010, 6, 16).isocalendar()[1]
term = (terms[week % len(terms)])
term = term.replace(".md", "")
link = "https://www.zerotoasiccourse.com/terminology/%s" % term

terms = 0
for row in analytics.rows:
    if 'terminology' in row.dimension_values[0].value: 
        terms += 1
        if term in row.dimension_values[0].value:
            print(row.dimension_values[0].value, row.metric_values[0].value, terms)
            break
terms = num2words(terms, to="ordinal_num")
twitter_text = "#ASIC terminology of the week!\n%s has been the %s most popular term in the last month.\n%s" % (term.capitalize(), terms, link)
print(twitter_text)

# post it
try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")


api.update_status(status = twitter_text)

