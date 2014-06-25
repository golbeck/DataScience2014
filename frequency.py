import sys
import json

def main():
    tweet_file = open(sys.argv[1])
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
        for everyword in words:
            total += 1
            if everyword in words_count.keys():                           
                words_count[everyword] += 1
            #if word is not in the list of words, add it and initialize counters
            elif everyword not in words_count:	
		        words_count[everyword]=1
		        
    #dictionary of frequencies
    freq = {}          
    for item in words_count:
        freq[item]=float(words_count[item])/total
#        sys.stdout.write(str(item) + ' ' + str(words_count[item]) + '\n')
        sys.stdout.write(str(item) + ' ' + str(freq[item]) + '\n')
        

if __name__ == '__main__':
    main()
