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
def fetch_loc():    
    tweet_file = open(sys.argv[2])
    tweet_loc = []
    
    sent_dict=build_dict()
#    print sent_dict
    
    state_dict=build_state_dict()
#    print state_dict
    
    for line in tweet_file:

        try:
            location=json.loads(line)['user']['location'].encode('utf-8')
            place=str(json.loads(line)['place'])
            
            if len(location) != 0:
                tweet_loc.append(location)
#                print location
            elif place != "None":
                tweet_loc.append(place)
#                print place
            else:
                tweet_loc.append("None")
#                print "None"
                
#            
#            print type(location)
#            if len(location) != 0:
#                print location
#                temp=location.split()
#                for item in temp:
#                    print item.rstrip(',.')
#            else:
#                print "No user location specified"
#                
#            place=str(json.loads(line)['place'])
#            if str(place) != "None":
#                print str(place)
#            else:
#                print "No place specified"
#                                
#            tweet_loc.append(json.loads(line)["text"].encode('utf-8'))
#            sys.stdout.write('test' + '\n')
#            sys.stdout.write(str(json.loads(line)["place"].encode('utf-8')) + '\n')
        except:
            pass
            
        
#        print len(tweet_loc)
    for item in tweet_loc:
        words=item.split()  
        for word in words:
            word=word.rstrip(',.')
        if word in state_dict.keys():
    #                    tweet_loc[item]=state_dict[word]
            print state_dict[word]
        else:
            print "not US tweet"
         
    print tweet_loc
                
        
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
def build_state_dict():
    statesfile = open(sys.argv[3])
    state_dict = {}
    for line in statesfile:
  		state1, state2  = line.split("\t") 
  		state_dict[state1] = state2.rstrip('\n')
    return state_dict
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
#        sys.stdout.write(str(total) + '\n')
    return tot_sentiment
###############################################
def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(afinnfile)
    lines(tweet_file)    
    ###############################################
    #build dictionary
    scores=build_dict()
    ###############################################
    #read-in tweets
    tweet_text=fetchsamples()
    ###############################################
    #read-in tweet location    
    tweet_loc=fetch_loc()
#    print type(tweet_loc)
#    print tweet_loc[0] 
    ###############################################
    #perform sentiment analysis   
    tot_sentiment=sentiment(scores,tweet_text)	

if __name__ == '__main__':
    main()
