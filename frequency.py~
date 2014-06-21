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
    atweetfile = open(sys.argv[1])
    tweet_text = []
    for line in atweetfile:
        try:
            tweet_text.append(json.loads(line)["text"].encode('utf-8'))
        except:
            pass

    total=0
    words_count={}
    for item in tweet_text:
        words = []
        words = item.split()
        #dictionary to track if a word is in the dic
        word_ind = {}
        for everyword in words:
            total += 1
            if everyword in words_count.keys():                           
                word_count[everyword] += 1
            #if word is not in the list of words, add it and initialize counters
            elif everyword not in words_count:	
		        words_count.append(everyword)
                words_count[everyword]=0
    #dictionary of frequencies
    freq = {}          
    for item in words_count:
        freq[item]=words_count[item]/total
        sys.stdout.write(str(item) + ' ' + str(freq[item]) + '\n')
	print str(len(words_count))

if __name__ == '__main__':
    main()
