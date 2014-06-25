import sys
import json
###############################################
def hw():
    print 'Hello, world!'
###############################################
def lines(fp):
    print str(len(fp.readlines()))
###############################################    
def fetchsamples():    
    tweet_file = open(sys.argv[2])
    tweet_text = []
    for line in tweet_file:
        try:
            tweet_text.append(json.loads(line)["text"].encode('utf-8'))
        except:
            pass
    return tweet_text
###############################################    
def build_dict():
    afinnfile = open(sys.argv[1])
    scores = {}
    for line in afinnfile:
  		term, score  = line.split("\t") 
  		scores[term] = float(score)
    return scores
###############################################    
def sentiment(scores,tweet_text):
    tot_sentiment=[]
    for item in tweet_text:
        words = []
        words = item.split()
        total = 0
        for everyword in words:
            if everyword in scores.keys():                           
                total += scores[everyword]
        tot_sentiment.append(total)
        sys.stdout.write(str(total) + '\n')
    return tot_sentiment
###############################################
def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    ###############################################
    #build dictionary
    scores=build_dict()
    ###############################################
    #read-in tweets
    tweet_text=fetchsamples()
    ###############################################
    #perform sentiment analysis   
    tot_sentiment=sentiment(scores,tweet_text)	

if __name__ == '__main__':
    main()
