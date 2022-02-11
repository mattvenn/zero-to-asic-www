#!/usr/bin/env python3
import requests
import argparse
from secrets import *
import tweepy
import glob
from num2words import num2words
from analytics import run_report
import os
import datetime

URL = "https://www.zerotoasiccourse.com"

class Term():

    def __init__(self, analytics, term_file, num_terms, args):
        self.file = term_file
        self.analytics = analytics
        self.num_terms = num_terms
        self.args = args

        self.url_end = self.file.replace('content/terminology/', '')
        self.url_end = self.url_end.lower().replace('.md', '')
        self.url = URL + "/terminology/" + self.url_end
        # add tracking
        self.url += '?utm_source=twitter&utm_medium=tweet&utm_campaign=terminology'

        self.term_rank = None
        rank = 0
        for row in self.analytics.rows:
            if 'terminology' in row.dimension_values[0].value: 
                stat_url = row.dimension_values[0].value
                #print(stat_url)
                stat_url = stat_url.replace(".md", "")
                stat_url = stat_url.replace("/terminology/", "")
                stat_url = stat_url.replace("/", "")
                stat_url = stat_url.lower()

                # skip blank urls
                if stat_url == '':
                    continue

                rank += 1
                if self.url_end == stat_url:
                    if self.term_rank is None:
                        if self.args.verbose:
                            print("found term %s at pos %d" % (self.url_end, rank))
                        self.term_rank = rank

        # get the title by reading the title definition from the file
        with open(term_file) as fh:
            for line in fh.readlines():
                if line.startswith('title: '):
                    title = line.split(':')[1].strip()
                    self.title = title.replace('"', '')
                    break


        ordinal_rank = num2words(self.term_rank, to="ordinal_num")
        self.twitter_text = "%s is the #ASIC terminology of the week!\n%s\n\nIn the last month, %s has been the %s most popular out of %d terms." % (
            self.title, self.url, self.title, ordinal_rank, self.num_terms)

    def __str__(self):
        return "%-40s %-20s %3s %s" % (self.file, self.title, self.term_rank, self.url)

    def test_url(self):
        request_response = requests.head(self.url)
        status_code = request_response.status_code
        if status_code in [200, 301]:
            print("ok")
        else:
            exit("problem with %s" % self.url)

    def tweet(self):
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication Successful")
        except:
            print("Authentication Error")

        # tweet it
        try:
            if api.update_status(status = self.twitter_text):
                print("Posted")
        except tweepy.error.TweepError as e:
            print(e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="tweet a term")
    parser.add_argument('--tweet', help="actually do the tweet", action='store_const', const=True)
    parser.add_argument('--week', help="force a specific week", type=int)
    parser.add_argument('--week-offset', help="add this number to the week number", type=int, default=0)
    parser.add_argument('--test-url', help="check url is ok", action='store_const', const=True)
    parser.add_argument('--verbose', help="debug", action='store_const', const=True)

    args = parser.parse_args()
    
    # fetch site's analytics - use function from the analytics.py file
    analytics = run_report(property_id)

    # get all the terminology files in order
    term_files = glob.glob("content/terminology/*md")
    term_files.remove("content/terminology/_index.md")
    # glob is non-deterministic!
    term_files = sorted(term_files, key=str.casefold)

    # build list of terms
    terms = []
    for term_file in term_files:
        term = Term(analytics, term_file, len(term_files), args)
        if args.test_url:
            term.test_url()
        terms.append(term)

    # pick the one to use
    if args.week is None:
        week = datetime.datetime.today().isocalendar()[1]
    else:
        week = args.week

    if args.verbose:
        print("this is week %d + offset %d = %s" % (week, args.week_offset, week + args.week_offset))

    week += args.week_offset

    term_of_the_week = terms[week % len(terms)]
    if args.verbose:
        print(term_of_the_week)
    print(term_of_the_week.twitter_text)

    if args.tweet:
        term_of_the_week.tweet()
