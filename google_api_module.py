# Importing libraries necessary for this module: 
# ----------------------------------------------
from google.cloud import language_v1
from twitter_api_module import * 
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "/Users/mac/Desktop/EC_601/Assignments/Project_2/credentials_google_api.json"
client = language_v1.LanguageServiceClient()


# Sentiment analysis function: 
def sentiment_analysis_tweets(texts):
    scores = []
    for text in texts:
        document = language_v1.Document(
            content=text,
            type_ = language_v1.Document.Type.PLAIN_TEXT)

        #sentiment feedback
        sentiment = client.analyze_sentiment(document=document).document_sentiment

        print('Text: {}'.format(text))
        print("Sentiment Score:", sentiment.score)

        scores.append(sentiment.score)
    

        #sentiment level
        if sentiment.score <=1 and sentiment.score>=0.3:
            print("Sentiment level: Positive")

        elif sentiment.score <0.3 and sentiment.score>= -0.3:
            print("Sentiment level: Neutral")

        elif sentiment.score<-0.3 and sentiment.score>=-1:
            print("Sentiment level: Negative")

    return scores


if __name__ == '__main__':

    # Asking user for input: 
    # --------------------
    print("What product do you want the tweets for:")
    product = input("")
    print("How many tweets do you want to pull:")
    numb_of_tweets = input("")
    print("="*20)
    numb_of_tweets = int(numb_of_tweets)
    tweets = twitter_extraction(product, numb_of_tweets) 
    sentiment_analysis_tweets(tweets["processed_tweets"])   