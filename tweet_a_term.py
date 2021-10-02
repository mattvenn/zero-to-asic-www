#!/usr/bin/env python3

from secrets import *
import tweepy
import glob
from num2words import num2words
from analytics import run_report
import os
import datetime

# fetch google analytics report
analytics = run_report(property_id)

# fetch the term of the week
os.chdir("content/terminology")
terms = glob.glob("*md")
week = datetime.date(2010, 6, 16).isocalendar()[1]
term = (terms[week % len(terms)])
term = term.replace(".md", "")
link = "https://www.zerotoasiccourse.com/terminology/%s" % term

# rank it
terms = 0
for row in analytics.rows:
    if 'terminology' in row.dimension_values[0].value: 
        terms += 1
        if term in row.dimension_values[0].value:
            print(row.dimension_values[0].value, row.metric_values[0].value, terms)
            term_rank = terms
term_rank = num2words(term_rank, to="ordinal_num")
twitter_text = "#ASIC terminology of the week!\n%s has been the %s most popular out of %d terms in the last month.\n%s" % (term.capitalize(), term_rank, terms, link)
print(twitter_text)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")

api.update_status(status = twitter_text)
