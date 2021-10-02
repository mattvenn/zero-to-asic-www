#!/usr/bin/env python3
from secrets import *
import tweepy
import glob
from num2words import num2words
from analytics import run_report
import os
import datetime

# fetch google analytics report, have to do this first because the secrets are in a local file
analytics = run_report(property_id)

# fetch the term of the week
os.chdir("content/terminology")
terms = glob.glob("*md")
week = datetime.date(2010, 6, 16).isocalendar()[1]
print("num terms found %d" % len(terms))
print("this is week %d" % week)
term = (terms[week % len(terms)])
term = term.replace(".md", "")
if term.isupper():
    term_name = term
else:
    term_name = term.capitalize()

link = "https://www.zerotoasiccourse.com/terminology/%s" % term
print(link)

# rank it
term_num = 0
for row in analytics.rows:
    if 'terminology' in row.dimension_values[0].value: 
        term_num += 1
        if term.lower() in row.dimension_values[0].value.lower():
            print("-" * 80)
            print("found term! at pos %d" % term_num)
            term_rank = term_num

term_rank = num2words(term_rank, to="ordinal_num")
twitter_text = "%s is the #ASIC terminology of the week!\n%s\nIn the last month, %s has been the %s most popular out of %d terms on https://ZeroToASICcourse.com/terminology" % (term_name, link, term_name, term_rank, len(terms))
print(twitter_text)
exit()
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
