#!/usr/bin/env python3
import requests
import argparse
from secrets import *
import tweepy
import glob
from atproto import Client
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
                if line.startswith('featured_image: '):
                    image = line.split(':')[1].strip()
                    self.image = title.replace('"', '')
                    break


        self.ordinal_rank = num2words(self.term_rank, to="ordinal_num")
        # add tracking
        self.twitter_text = "%s is the #ASIC terminology of the week!\n%s\n\nIn the last month, %s has been the %s most popular out of %d terms." % (
            self.title, self.url + '?utm_source=twitter&utm_medium=tweet&utm_campaign=terminology', self.title, self.ordinal_rank, self.num_terms)

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
        client = tweepy.Client(
            consumer_key=api_key, consumer_secret=api_key_secret,
            access_token=access_token, access_token_secret=access_token_secret)

        # tweet it
        response = client.create_tweet( text=self.twitter_text)
        print(response)

    def skeet(self):
        from atproto import Client
        from atproto import models
        from atproto import client_utils

        client = Client()
        client.login(bluesky_handle, bluesky_password)

        if args.verbose:
            print("image is " + self.image)
        with open('static/' + self.image, 'rb') as f:
          img_data = f.read()

        self.skeet_text = client_utils.TextBuilder()
        self.skeet_text.text("%s is the " % self.title)
        self.skeet_text.link("#ASIC", "https://bsky.app/hashtag/asic")
        self.skeet_text.text(" terminology of the week!\n")
        self.skeet_text.text("In the last month, %s has been the %s most popular out of %d terms." % (self.title, self.ordinal_rank, self.num_terms))

        thumb = client.upload_blob(img_data)
        embed = models.AppBskyEmbedExternal.Main(
            external=models.AppBskyEmbedExternal.External(
                title=self.title,
                description="%s is the ASIC terminology of the week!\n\n" % self.title,
                uri=self.url + '?utm_source=bluesky&utm_medium=tweet&utm_campaign=terminology',
                thumb=thumb.blob,
            )
        )
        
        post = client.send_post(self.skeet_text, embed=embed)
        print(post)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="tweet a term")
    parser.add_argument('--tweet', help="actually do the tweet", action='store_const', const=True)
    parser.add_argument('--skeet', help="actually do the skeet", action='store_const', const=True)
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

    if args.skeet:
        term_of_the_week.skeet()
