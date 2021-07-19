#!/usr/bin/env python
# coding: utf-8
'''
Lyrics Predictor
'''

import requests
from bs4 import BeautifulSoup
import re
import sys
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split as tts

def scrape_links(url):
    '''
    Scrapes the links to all songs of an artist provided their page on lyrics.com.
    
    Parameters
    ----------
    url : str
        the url of artist page on lyrics.com

    Returns
    -------
    list
        a list of strings with the links to the all song lyrics on the artist page on lyrics.com
    '''
    response = requests.get(url)
    html_artist = response.text
    artist_name = re.findall('Albums by <strong>([^<]+)', html_artist)[0]
    soup_artist = BeautifulSoup(html_artist)#, features="lxml")
    html_links = soup_artist.find_all(attrs={'class': 'tal qx'})
    lyrics_links = []
    song_titles = []
    for entry in html_links:
        str_entry = str(entry.find_all('a')[0])
        path_end, song_title = re.findall('\/l[^<]+', str_entry)[0].split(sep='">')
        if song_title not in song_titles: # this removes duplicates
            lyrics_links.append('https://www.lyrics.com' + path_end)
            song_titles.append(song_title)
    return lyrics_links, artist_name


def scrape_lyrics(url):
    '''
    Scrapes the lyrics of all songs of an artist provided their page on lyrics.com.
    The lyrics are then saved as separate files in a new diretcory in the current working directory.
    
    Parameters
    ----------
    url : str
        the url of artist page on lyrics.com
    '''
    lyrics_links, artist_name = scrape_links(url)
    for i, song in enumerate(lyrics_links, 1):
        response_song = requests.get(song)
        html_song = response_song.text
        soup_song = BeautifulSoup(html_song)#, features="lxml")
        html_lyrics = str(soup_song.find(attrs={'class': "lyric-body"}))
        if html_lyrics == 'None':
            continue # skips empty lyrics
        else:
            lyrics = re.sub('<.+?>+?', '', html_lyrics)
            lyrics = re.sub('\[', '', lyrics)
            lyrics = re.sub('\]', '', lyrics) # TODO: simplify regex
            num_len = len(str(len(lyrics_links))) # length of number of songs
            with open('./songs/' + artist_name.replace(' ', '_') + '_' + str(i).zfill(num_len) + '.txt', 'w') as f:
                #zfill(num_len) makes sure there are enough leading 0's before the number to sort files easily.
                f.writelines(lyrics)
            #list_lyrics_artist(artist_name, i)

def list_lyrics_artist(artist_name, num_songs):
    '''
    Creates two lists of strings: one with the i lyrics and another with the name of the artist i times.
    '''
    artist_list = [artist_name for i in range(num_songs)]
    num_len = len(str(num_songs))
    lyrics_list = []
    for i in range(1, num_songs + 1):
        with open('./songs/' + artist_name.replace(' ', '_') + '_' + str(i).zfill(num_len) + '.txt', 'r') as f:
            lyrics_list.append(f.read())
    return lyrics_list, artist_list

def build_model(X, y):
    '''
    Trains Logistic Regression model
    '''
    Xtrain, Xtest, ytrain, ytest = tts(X, y)
    cv = CountVectorizer()



## Main Program:

url = 'https://www.lyrics.com/artist/Laurie-Anderson/3545'
X = []
y = []

lyrics_list, artist_list = list_lyrics_artist()
X.append(lyrics_list)
y.append(artist_list)
