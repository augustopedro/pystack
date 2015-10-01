#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


# list of phrases
phrases = []

# read phrases from file
with open('funny.txt', 'r') as myfile:
    for line in myfile:
        phrases.append(line)


def get_funny_phrase():
    u''' Get one funny funny_phrase from the list of funny_phrases'''
    return phrases.pop()