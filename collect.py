#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2
from lxml import html
import requests
from urllib2 import urlopen


'''
TODO
Coletar mais frases de forma dinamica (tweets?)
'''

def collect_funny_phrases(link):
    u'''verificar a existencia de espaco em branco no arquivo na hora de realizar a leitura
    fazer paginacao em outras paginas para pegar mais arquivos
    limitar o get de mensagens para mensagens menores que 140 caracteres
    '''
    
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; '
    'en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    
    headers = {
        'User-Agent':user_agent
    } 

    request = urllib2.Request(link, None, headers) # The assembled request
    response = urllib2.urlopen(request)
    data = response.read() # The data u need

    # mount tree
    tree = html.fromstring(data)

    # get posts text
    posts = tree.xpath('//div[@class="boxyPaddingBig"]//span[@class="bqQuoteLink"]//a/text()')

    with open('funny_en.txt', 'a') as myfile:
        for post in posts:
            if len(post) <= 120:
                myfile.write(post+'\n')

def function():
    pass


def collect_rates():
    u'''Get the dolar rates at the yahoo server using YQL'''

    # Query of search
    query = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22USDBRL%22%2C%22EURBRL%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='

    # get currency from yahoo
    data = json.load(urlopen(query))

    # returns the dolar rate converted to BRL
    return str(data['query']['results']['rate'][0]['Bid'])

for i in range (13):
    if i == 0:
        collect_funny_phrases('http://www.brainyquote.com/quotes/topics/topic_finance.html')
    else:
        collect_funny_phrases('http://www.brainyquote.com/quotes/topics/topic_finance'+str(i)+'.html')

