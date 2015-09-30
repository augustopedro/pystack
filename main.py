#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time
from tweepy.error import TweepError
from funny import funny_phrase_down, funny_phrase_up
from collect import get_rates
 
# OAuth process, using the keys and tokens (add you own keys)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# historic of rates
rates = [0]

def update_status(funny_phrase):
    u''' Update user's status on twitter, gets a funny phrase '''
    try:
        api.update_status(status='Dólar tá '+get_rates()+' BRL. '+funny_phrase)
        print('Status updated')

    except TweepError, e:
        print('Duplicated status.')


def main():

    while True: 
        
        # get rates
        rate = get_rates()

        if rate == rates[-1]:
            update_status('Nada mudou. Continuamos fodidos.')
        if rate < rates[-1]:
            update_status(funny_phrase_down())
        else:
            update_status(funny_phrase_up())

        rates.append(rate)
        print rates

        # Waits for one minute
        time.sleep(60)


if __name__ == '__main__':
    main()
