import sys
import json

def new_sentiment(words_new_scores,words_new_count):
    for x in words_new_scores.keys():
        temp=float(words_new_scores[x])/words_new_count[x]
        sys.stdout.write(str(x) + ' ' + str(temp) + '\n')
        
def main():
    
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
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
    ###############################################
    words_new_scores={}
    words_new_count={}
    for item in tweet_text:
        words=[]
        words = item.split()
        total = 0
        #dictionary to track if a word has already been counted in the current tweet
        word_ind = {}
        
        ###############################################
        for everyword in words:
            word_ind[everyword]=0
            if everyword in scores.keys():                           
                total += scores[everyword]
            #if word is not in the list of new words, add it and initialize counters
            elif everyword not in words_new_scores.keys():
                words_new_scores[everyword]=0
                words_new_count[everyword]=0
                    
        ###############################################
        #set current tweet sentiment to words not in dictionary
        #only count the word once per tweet
        for everyword in words:
            if everyword in words_new_scores.keys():
                if word_ind[everyword]==0:
                    words_new_scores[everyword] += total
                    words_new_count[everyword] += 1
                    word_ind[everyword]=1
                    
    new_sentiment(words_new_scores,words_new_count)

if __name__ == '__main__':
    main()
