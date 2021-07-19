#!/usr/bin/env python
# coding: utf-8
"""
Dummy lyrics predictor
"""

# 1. imports
import sys

# 2. constants
BEATLES_WORDS = ['submarine', 'yeah', 'love']
EMINEM_WORDS = ['detroit', 'gun', 'lose', 'yourself']

# 3. function definitions
def count_words(text, words1, words2):
    """counts words in two sample vocabularies"""
    a, b = 0, 0

    for word in text.lower().split():
        if word in words1:
            a += 1
        if word in words2:
            b += 1
    return a, b  # <-- tuple


def predict_artist(lyrics):
    """returns the probable name of the artist given some text"""
    b, e = count_words(lyrics, BEATLES_WORDS, EMINEM_WORDS)

    if b > e:
        return 'beatles'
    elif e > b:
        return 'eminem'
    else:
        return 'no idea'


# 4. main program
filename = sys.argv[1]

text = open(filename).read()
print(predict_artist(text))

"""
# 5. to read in multiple files from one directory
import os

corpus = []
for fn in os.listdir('/home/kristian/Downloads/dummy_predictor'):
    if fn.endswith('txt'):
        text = open(filename).read()
        corpus.append(text)
print(corpus)
"""