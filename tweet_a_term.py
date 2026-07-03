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

    def __init__(self, term_file, num_terms, args, rank_lookup):
        self.file = term_file
        self.num_terms = num_terms
        self.args = args

        self.url_end = self.file.replace('content/terminology/', '')
        self.url_end = self.url_end.lower().replace('.md', '')
        self.url = URL + "/terminology/" + self.url_end

        # fall back to last place if the term never showed up in analytics
        # (e.g. brand new term with no traffic yet)
        self.term_rank = rank_lookup.get(self.url_end, num_terms)
        if self.args.verbose:
            print("found term %s at pos %d" % (self.url_end, self.term_rank))

        # get the title by reading the title definition from the file
        with open(term_file) as fh:
            for line in fh.readlines():
                if line.startswith('title: '):
                    title = line.split(':')[1].strip()
                    self.title = title.replace('"', '')
                if line.startswith('featured_image: '):
                    image = line.split(':')[1].strip()
                    self.image = image.replace('"', '')

        if args.verbose:
            print(f"{term_file},{self.title},{self.image}")

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

    # normalize the url each term file would live at, so we can recognise
    # analytics rows that correspond to a term that still exists
    known_url_ends = set()
    for term_file in term_files:
        url_end = term_file.replace('content/terminology/', '')
        url_end = url_end.lower().replace('.md', '')
        known_url_ends.add(url_end)

    # rank terms by popularity, counting each known term at most once -
    # analytics can contain multiple/stale rows (renamed or deleted terms,
    # trailing-slash or query-string variants) which must not inflate rank
    rank_lookup = {}
    rank = 0
    for row in analytics.rows:
        if 'terminology' not in row.dimension_values[0].value:
            continue
        stat_url = row.dimension_values[0].value
        stat_url = stat_url.replace(".md", "")
        stat_url = stat_url.replace("/terminology/", "")
        stat_url = stat_url.replace("/", "")
        stat_url = stat_url.lower()

        if stat_url == '' or stat_url not in known_url_ends:
            continue
        if stat_url in rank_lookup:
            continue

        rank += 1
        rank_lookup[stat_url] = rank

    # build list of terms
    terms = []
    for term_file in term_files:
        term = Term(term_file, len(term_files), args, rank_lookup)
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
