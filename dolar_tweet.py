#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib
import tweepy

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


r = urllib.urlopen('http://bbv.infosel.com/bancomerindicators/index.aspx')

soup = BeautifulSoup(r)

data = []

table = soup.find('table')
table_body = table.find('tbody')

line = 0

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
    line += 1
    if line == 5:
        break

dolar_venta = data[4][3]

message = data[4][2] + " " + dolar_venta

api.update_status(status=message)
