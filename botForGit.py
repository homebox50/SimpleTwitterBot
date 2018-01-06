import twitter, tweepy, random

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
#argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = #CONSUMER KEY GOES HERE
CONSUMER_SECRET = #CONSUMER SECRET GOES HERE
ACCESS_KEY = #ACCESS KEY GOES HERE
ACCESS_SECRET = #ACCESS SECRET GOES HERE
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

 

choice1 = #list of words go here
choice2 = #list of words go here
choice3 = #list of words go here


i = 0
while i < 20:
    word1 = random.choice(choice1)
    word2 = random.choice(choice2)
    word3 = random.choice(choice3)

    sentence = #INSERT TEST SENTENCE HERE

    api.update_status(sentence)
    i = i + 1
    time.sleep(300)#Tweet every 5(?) minutes
    
 

    
