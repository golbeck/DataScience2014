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
    #build dictionary
    afinnfile = open(sys.argv[1])
    scores = {}
    for line in afinnfile:
  		term, score  = line.split("\t") 
  		scores[term] = float(score)

    ###############################################
    atweetfile = open(sys.argv[2])
    tweet_text = []
    for line in atweetfile:
        try:
            tweet_text.append(json.loads(line)["text"].encode('utf-8'))
        except:
            pass

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
	

if __name__ == '__main__':
    main()
