#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

funny_phrases_down = [
    "Baixou o dolar, mais um pouco e #partiuUSA",
    "Com essa cotação dá para comprar ação da petrobrás",
    "Pensando em começar a investir pesado no dólar",
    "Não sei se compro dólar ou se compro ação da petrobrás"
    "O impossivel aconteceu. O dolar caiu."
]

funny_phrases_up = [
    "Aumentou o dolar, tamo fodido.",
    "Valorizou o dólar #partiuUSA",
    "Vamos todos virar americanos. #USA",
    "Subiiiiiiiiuuuuuuuu #dolar",
    "Fodeu mais ainda. Dolar Subiiiiiiiiuuuuuuuu...."
]


def funny_phrase_down():
    u''' Get one funny funny_phrase from the list of funny_phrases'''
    return random.choice(funny_phrases_down)


def funny_phrase_up():
    u''' Get one funny funny_phrase from the list of funny_phrases'''
    return random.choice(funny_phrases_up)
