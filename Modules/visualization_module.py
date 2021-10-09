# Importing libraries necessary for this module: 
# ----------------------------------------------
import matplotlib.pyplot as plt
from twitter_api_module import * 
from google_api_module import * 
import sys 
from wordcloud import WordCloud

# Plot visualization from sentiment analysis: 
def main():

    # Running input through models for twitter and google api
    tweets = twitter_extraction(product, numb_of_tweets) 
    scores = sentiment_analysis_tweets(tweets["processed_tweets"])   

    # Count for tweets in each category 
    v1 = 0
    v2 = 0 
    v3 = 0 

    for score in scores:
        if score <=1 and score>=0.3:
            v1=v1+1
        elif score<0.3 and score>=-0.3:
            v2=v2+1
        elif score<-0.3 and score>=-1:
            v3=v3+1

   # Plot pie chart: 
    # --------------
    labels = 'Positive', 'Neutral', 'Negative'
    sizes = [v1,v2,v3]
    colors = ['yellowgreen', 'lightcyan','red']
    explode = (0, 0, 0)  

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Sentiment Analysis Result: {}'.format(product))
    plt.axis('equal')
    plt.show()

    # Plot wordcloud: 
    # ---------------
    wordcloud = WordCloud(
        max_font_size=50, max_words=100, background_color="white").generate(
            ' '.join(tweets["processed_tweets"]))
    plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == '__main__':

    # Asking user for input: 
    # -------------------- 
    print("What product do you want the tweets for:")
    product = input("")
    print("How many tweets do you want to pull:")
    numb_of_tweets = input("")
    print("="*20)
    numb_of_tweets = int(numb_of_tweets)
    main()