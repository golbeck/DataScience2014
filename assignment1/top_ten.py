import sys
import json
###############################################    
def hashtag_analysis():    
    #open file of tweet
    tweet_file = open(sys.argv[1])
    #hash tag dictionary
    hashtags={}
        
    #get locations for the tweets
    for line in tweet_file:
        try:
            hashtag = json.loads(line)['entities']['hashtags']
            if len(hashtag) != 0:
                for i in range(0,len(hashtag)-1):
                    word=hashtag[i]['text'].encode('utf-8')
                    if word in hashtags:
                        hashtags[word]+=1.0
                    else:
                        hashtags[word]=1.0
        except:
            pass
              
    hashtags_sort= sorted(hashtags, key=hashtags.get, reverse=True) 
    for i in range(0,10):   
        temp=hashtags_sort[i]
        sys.stdout.write(str(temp) + ' ' + str(hashtags[temp]) + '\n')    
        
    return hashtags_sort
###############################################
def main():
    hashtag_analysis()

if __name__ == '__main__':
    main()
