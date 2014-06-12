import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)    
    ###############################################
    afinnfile = open(sys.argv[1])
    scores = {}
    for line in afinnfile:
  		term, score  = line.split("\t") 
  		scores[term] = float(score)
#    print scores.items()

    ###############################################
    atweetfile = open(sys.argv[2])
    tweets = []
    for line in atweetfile:
        try:
            tweets.append(json.loads(line))
        except:
            pass
            
    print len(tweets)
    tweet = tweets[0]
    print tweet
	

if __name__ == '__main__':
    main()
