import oauth2 as oauth
import urllib2 as urllib
import json
import re
import sys
###############################################
#build dictionary
afinnfile = open("AFINN-111.txt")
scores = {}
for line in afinnfile:
    term, score  = line.split("\t") 
    scores[term] = float(score)
###############################################
#read in tweets and save into a dictionary
atweetfile = open("output.txt")
#tweets = []
tweet_text = []
for line in atweetfile:
    try:
#        tweets.append(json.loads(line))
        tweet_text.append(json.loads(line)["text"].encode('utf-8'))
    except:
        pass

tot_sentiment=[]
for item in tweet_text:
    words = []
    words = item.split()
    total = 0.0
    for everyword in words:
        if everyword in scores.keys():                           
            total += scores[everyword]
    tot_sentiment.append(total)
    sys.stdout.write(str(total) + '\n')
