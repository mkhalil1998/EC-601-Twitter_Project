# Importing libraries necessary for this module: 
# ----------------------------------------------

from numpy.core.numeric import extend_all
import tweepy
import pandas as pd
import numpy as np
import re
from nltk.tokenize import WordPunctTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from datetime import datetime, timedelta
import os 
import nltk
from nltk import word_tokenize


# Twitter Api Credentials
consumerK = "Enter consumer key"
consumerS = "Enter consumer secret"
accessT = "Enter access key"
accessS = "Enter access secret"

# Function to remove stopwords
stop_words = set(stopwords.words('english'))

def preprocess_tweet_text(tweet):
    # Remove stopwords
    tweet_tokens = word_tokenize(tweet)
    filtered_words = [w for w in tweet_tokens if not w in stop_words]

    return " ".join(filtered_words)

# Function to extract tweets: 
def twitter_extraction(twitter_name, number_of_tweets):

    # Twitter Authorization: 
    # ---------------------
    # Create the authentication object
    auth = tweepy.OAuthHandler(consumerK, consumerS)
    # Set the access token and access token secret
    auth.set_access_token(accessT, accessS)
    # Creating the API object while passing in auth information, wait_on_rate_limit= True to allow extraction without passing limit
    api = tweepy.API(auth, wait_on_rate_limit= True)

    # Extract tweets from the twitter user
    # ------------------------------------
    posts = tweepy.Cursor(api.search,
              q=twitter_name,
              lang="en", 
              tweet_mode = "extended").items(number_of_tweets)

    # Create a dataframe with a column called Tweets
    # ----------------------------------------------
    df = pd.DataFrame([tweet.full_text for tweet in posts], columns = ["tweets"])

    # Cleaning the text from tweets
    # -----------------------------
    # - Cleaning the text for tweets
    df['processed_tweets'] = df['tweets'].str.lower()\
          .str.replace('(@[a-z0-9]+)\w+',' ')\
          .str.replace('(http\S+)', ' ')\
          .str.replace('([^0-9a-z \t])',' ')\
          .str.replace(' +',' ')

    # - Remove stop words
    df['processed_tweets'] = df["processed_tweets"].apply(preprocess_tweet_text)

    # Printing results: 
    # ----------------
    print("Most recent Tweets:")
    print(df)
    print("="*20)

    return df


if __name__ == '__main__':

    # Asking user for input: 
    # ---------------------
    print("What product do you want the tweets for:")
    product = input("")
    print("How many tweets do you want to pull:")
    numb_of_tweets = input("")
    numb_of_tweets = int(numb_of_tweets)
    tweets = twitter_extraction(product, numb_of_tweets) 
