import json
from urllib2 import urlopen

def get_rates():
    u'''Get the dolar rates at the yahoo server using YQL'''

    # Query of search
    query = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22USDBRL%22%2C%22EURBRL%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='

    # get currency from yahoo
    data = json.load(urlopen(query))

    return str(data['query']['results']['rate'][0]['Bid'])