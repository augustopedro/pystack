import tweepy
from tweepy.error import TweepError
import json
from urllib2 import urlopen
import os
import time
 
# Consumer keys and access tokens, used for OAuth (Twitter)
consumer_key = 'FM4O9XlzGfUJXflKT4WA'
consumer_secret = 'e8sv9W7g3SYJtSVytHqCYcueK7kfRvQQBk6Zw0gVBJk'
access_token = '44702733-1qTT1wdqCq3vBvaFZcPpSRnyIsLgEyOIwRyD61i6J'
access_token_secret = 'gsmt1NeA3I6g1UbHloKjVrF8zJYNAfdCdGzFa0NpLJ8'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def get_rates():
    u'''Get the dolar rates at the yahoo server'''

    # Query of search
    query = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22USDBRL%22%2C%22EURBRL%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='

    # get currency from yahoo
    data = json.load(urlopen(query))

    return str(data['query']['results']['rate'][0]['Bid'])


def main():

    while True: 
    
        try:
            # Sample method, used to update a status
            api.update_status(status='Hi! This is an update status for you to know the dolar cotation in Brazilian Reais. And it is: '+get_rates()+' BRL')
            print('Status updated')

        except TweepError, e:
            print('Duplicated status.')

        # Waits for one minute
        time.sleep(60)


if __name__ == '__main__':
    main()
