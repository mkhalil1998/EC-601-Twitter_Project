# Importing libraries necessary for this module: 
# ----------------------------------------------
from tokenize import Number
from numpy.core.numeric import extend_all
from numpy.matrixlib import defmatrix
import pandas as pd
import tweepy
import sys

'''
Two functions: 
--------------
(1) authu, used to authenticate twitter api credentials
input: credentials
output: api 

(2) search_tweets, used to return most recent tweets for a specific query 
input: api, q(query), num_of_tweets
output: tweets and errors 

'''

# Twitter Api Credentials
consumerK = ""
consumerS = ""
accessT = ""
accessS = ""

# Anuthentication
def authu():

    auth = tweepy.OAuthHandler(consumerK, consumerS)
    auth.set_access_token(accessT, accessS)
    api = tweepy.API(auth, wait_on_rate_limit= True)
    return api


def search_tweets(api, q , num_of_tweets):
    errors = []
    try:
        #posts =  api.search(q, lang='en', count = num_of_tweets)
        posts = tweepy.Cursor(api.search,
              q,
              lang="en", 
              tweet_mode = "extended").items(num_of_tweets)
    except tweepy.TweepError as error:
        errors.append(search_tweets.__name__ + ': ' + str(error))

    df = pd.DataFrame([tweet.full_text for tweet in posts], columns = ["tweets"])

    if len(df) != 0:
        print('Results founds')
    else:
        errors.append(search_tweets.__name__ + ': ' + 'No Results Found')
        print(errors)

    return (df,errors)


if __name__ == '__main__':

    api = authu()
    (df, errors) = search_tweets(api = api, q='Airpods', num_of_tweets = 10)
    print('Errors:')
    print(errors)
    print('Tweets:')
    print(df)

