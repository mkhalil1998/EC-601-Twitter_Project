from google.cloud import language_v1
from TwitterProject_Phase1a import * 
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "/Users/mac/Desktop/EC_601/Assignments/Project_2/credentials_google_api.json"
client = language_v1.LanguageServiceClient()

# Sentiment analysis function
def sentiment_analysis_tweets(texts):
    scores = []
    # Extracts tweets from dataframe 
    for text in texts:
        document = language_v1.Document(
            content=text,
            type_ = language_v1.Document.Type.PLAIN_TEXT)

        #sentiment feedback
        sentiment = client.analyze_sentiment(document=document).document_sentiment

        print('Text: {}'.format(text))
        print("Sentiment Score:", sentiment.score)
    
        # Appends score to list scores 
        scores.append(sentiment.score)

        # Sentiment level
        if sentiment.score <=1 and sentiment.score>=0.7:
            print("Sentiment level: Very Positive")

        elif sentiment.score <0.7 and sentiment.score>=0.3:
            print("Sentiment level: Positive")

        elif sentiment.score<0.3 and sentiment.score>=-0.3:
            print("Sentiment level: OK")

        else:
            print("Sentiment level: Negative")
    return scores

if __name__ == '__main__':
    #pass in the username of the account you want to download
    tweets = twitter_extraction("WhiteHouse", 10) 
    sentiment_analysis_tweets(tweets["Tweets"])   