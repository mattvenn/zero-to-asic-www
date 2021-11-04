#!/usr/bin/env python3
import argparse
from secrets import *
import tweepy
import glob
from num2words import num2words
from analytics import run_report
import os
import datetime

def fetch_analytics():
    # fetch google analytics report, have to do this first because the secrets are in a local file
    analytics = run_report(property_id)
    return analytics

def get_term_of_the_week(analytics, week=None):
    # fetch the term of the week
    os.chdir("content/terminology")
    terms = glob.glob("*md")

    # glob is non-deterministic!
    terms.sort()

    if week is None:
        week = datetime.datetime.today().isocalendar()[1]

    print("num terms found %d" % len(terms))
    print("this is week %d" % week)
    term = (terms[week % len(terms)])
    term = term.replace(".md", "")

    print("looking for %s" % term)

    # rank it
    num_terms = 0
    term_rank = None
    for row in analytics.rows:
        if 'terminology' in row.dimension_values[0].value: 
            num_terms += 1
            stat_url = row.dimension_values[0].value
            print(stat_url)
            stat_url = stat_url.replace(".md", "")
            stat_url = stat_url.replace("/terminology/", "")
            stat_url = stat_url.replace("/", "")
            # sometimes GA lists 2 urls that go to the same term like /drc & /DRC. So only take the first one
            if term_rank is None:
                if term.lower() == stat_url.lower():
                    print("-" * 80)
                    print("found term! at pos %d" % num_terms)
                    term_rank = num_terms

    return term, term_rank, num_terms

def create_tweet(term, term_rank, num_terms):
    if term.isupper():
        term_name = term
    else:
        term_name = term.capitalize()
    term_rank = num2words(term_rank, to="ordinal_num")
    link = "https://www.zerotoasiccourse.com/terminology/%s" % term.lower() # even if the page name is DRC, the link is drc
    twitter_text = "%s is the #ASIC terminology of the week!\n%s\n\nIn the last month, %s has been the %s most popular out of %d terms." % (term_name, link, term_name, term_rank, num_terms)
    print(twitter_text)

    return twitter_text

def tweet_it(tweet_text):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication Successful")
    except:
        print("Authentication Error")

    try:
        if api.update_status(status = twitter_text):
            print("Posted")
    except tweepy.error.TweepError as e:
        print(e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="tweet a term")
    parser.add_argument('--tweet', help="actually do the tweet", action='store_const', const=True)
    parser.add_argument('--week', help="force a specific week", type=int)

    args = parser.parse_args()
    
    analytics = fetch_analytics()
    term, term_rank, num_terms = get_term_of_the_week(analytics, args.week)
    tweet = create_tweet(term, term_rank, num_terms)

    if args.tweet:
        tweet_it(tweet)
