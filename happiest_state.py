import sys
import json
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
def fetch_loc():    
    #open file of tweet
    tweet_file = open(sys.argv[2])
    #text in the tweet file
    tweet_text=fetchsamples()
    tweet_loc = []
    #sentiment dictionary
    scores=build_dict()
    #state dictionary
    state_dict=build_state_dict()
    state_sentiment={}
    state_count={}
    #for each state, initialize the sentiment to 0
    for item in state_dict:
        state_sentiment[item]=0
    #for each state, initialize the counter to 0
    for item in state_dict:
        state_count[item]=0
        
    #get locations for the tweets
    for line in tweet_file:
        try:
            location=json.loads(line)['user']['location'].encode('utf-8')
            place=str(json.loads(line)['place'])
            
            if len(location) != 0:
                tweet_loc.append(location)
            elif place != "None":
                tweet_loc.append(place)
            else:
                tweet_loc.append("None")
        except:
            pass
            
    #use list to determine if tweet ocurred in US state    
    for i in range(0,len(tweet_loc)):
        words=tweet_loc[i].split()  
        for word in words:
            word=word.rstrip(',.')
            #if a US state is in the location, perform sentiment analysis
            if word in state_dict:
                state_sentiment[word]+=sentiment(scores,tweet_text[i])
                state_count[word]+=1
                break
                
    #compute average sentiment score for each state
    for i in state_dict:
        if state_count[i]>0:
            state_sentiment[i]=float(state_sentiment[i])/state_count[i]
    
    #sort the dictionary from most to least happy state
    state_sentiment_sort= sorted(state_sentiment, key=state_sentiment.get, reverse=True)   
#    for i in state_sentiment_sort: 
##        sys.stdout.write(str(i) + ' ' + str(state_sentiment[i]) + '\n')    
#        sys.stdout.write(str(i) + '\n')    
    sys.stdout.write(str(state_sentiment_sort[0]) + '\n')     
    return tweet_loc
###############################################    
def build_dict():
    afinnfile = open(sys.argv[1])
    scores = {}
    for line in afinnfile:
  		term, score  = line.split("\t") 
  		scores[term] = float(score)
    return scores
###############################################    
#dictionary of state abbreviations
def build_state_dict():
    state_dict={'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME','MD','MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'}
    return state_dict
###############################################   
#return a list of tweet text samples 
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
#perform sentiment analysis on a single tweet
def sentiment(scores,tweet_text):
    words=[]
    words = tweet_text.split()
    total = 0
    for everyword in words:
        if everyword in scores.keys():                           
            total += scores[everyword]
    return total
###############################################
def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    ###############################################
    #output sentiment scores for each state   
    tweet_loc=fetch_loc()

if __name__ == '__main__':
    main()
