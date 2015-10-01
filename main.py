#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time
from tweepy.error import TweepError
from funny import get_funny_phrase
from collect import get_rates
 
# OAuth process, using the keys and tokens (add you own keys)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def update_status(rate, funny_phrase):
    u''' Update user's status on twitter, gets a funny phrase '''
    try:
        api.update_status(status='1 USD = {} BRL. {}'.format(rate, funny_phrase))
        print('Status updated')

    except TweepError, e:
        print('Duplicated status.')

def main():

    while True: 
        
        # get rates
        rate = get_rates()

        # update status on twitter
        update_status(rate, get_funny_phrase())

        # Waits for one minute
        time.sleep(60)


if __name__ == '__main__':
    main()
