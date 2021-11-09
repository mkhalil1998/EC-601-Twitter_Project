# Importing libraries
import tweepy
import pandas as pd
import numpy as np
import re
from nltk.tokenize import WordPunctTokenizer
from datetime import datetime, timedelta

# Twitter Api Credentials
consumerKey = "Enter the consumer_key"
consumerSecret = "Enter the consumer_secret"
accessToken = "Enter the access_key"
accessTokenSecret = "Enter the access_secret"


def clean_tweets(text): 
    # Removing #tag
    cleaned_text = re.sub('#', '', text)
    #Removing @mentions
    cleaned_text = re.sub('@[A-Za-z0–9]+', '', text) 
    # Removing hyperlink
    cleaned_text = re.sub('https?:\/\/\S+', '', text) 

    return cleaned_text

def twitter_extraction(twitter_name, number_of_tweets):

    # Create the authentication object
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    # Set the access token and access token secret
    auth.set_access_token(accessToken, accessTokenSecret)
    # Creating the API object while passing in auth information, wait_on_rate_limit= True to allow extraction without passing limit
    api = tweepy.API(auth, wait_on_rate_limit= True)

    # Extract tweets from the twitter user
    posts = api.user_timeline(screen_name=twitter_name, count = number_of_tweets, lang ="en", tweet_mode="extended")

    # Create a dataframe with a column called Tweets
    df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])

    # Cleaning the text from tweets
    df['Tweets'] = df['Tweets'].apply(clean_tweets)
    
    # Printing results: 
    print("Most recent 10 Tweets:")
    print(df)

    return df


if __name__ == '__main__':
    #pass in the username of the account you want to download
    twitter_extraction("@Cristiano", 10) 
