#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


''''
for using text as json
import json

tweets_data_path = './json/dilma.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
        print(json.dumps(tweet, indent=4))
    except:
        continue
'''

# list of phrases
phrases = []

# read phrases from file
with open('funny_pt.txt', 'r') as myfile:
    for line in myfile:
        phrases.append(line)


def get_funny_phrase():
    u''' Get one funny funny_phrase from the list of funny_phrases'''
    return phrases.pop()