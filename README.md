# EC-601-Projects

## Project 2: Twitter Project


Phase 1 a: Exploring the twitter API
--------

TwitterProject-Phase1.py allows the user to extract the most recent twitter posts for a particular user. 
The code also cleans the data so that it is ready for the next step of NLP. 

Testing: The code was tested with extracting the most recent twitter posts from Cristiano Ronaldo and they were compared to the tweets on twitter.


Phase 1 b: Exploring the Google NLP API 
--------

TwitterProject-Phase1b.py allows the user to use the extracted text from twitter that can be done using TwitterProject-Phase1.py and input it to the new function entiment_analysis_tweets. According to the generated sentiment score, the tweet is categorized into one of the sentiment levels. 
 
 - 0.3 - 1 -> Positive 
 - 0.3 - -0.3 -> Neutral  
 - -0.3 - -1 -> Negative 
 
Testing: The code was tested with extracting the 10 most recent twitter posts from the White House and each post was given a sentiment level. 

Phase 2: Product Mission
--------

### User:
As a sales manager, I want to understand if customers are enjoying the product so that I can pin point improvements for the next release. I don't want to rely only on amazon/google reviews but also wants to analyze tweets. By looking at tweets about the product, and focus mainly on the ones that are tagged as negative by the sentiment analysis API. 

As a customer, I am interested in buying a product and want to get an idea on what people think about it, as well as take a closer look at tweets that have both have very positive or very negative sentiment. 

### MVP: 
The product should be able to provide the user with the following:  
 - Tweets about specified product
 - Sentiment Analysis for generated tweets 

In addition to this main two requirements, I believe that information such as date and location can provide also important insights to the user, these can be added to the both the query as well as outputs. 

### Modules: 

The goal of the project is to provide the user the flexibility of analyzing tweets for a particular product through a general lense or a more detailed view, depending on the needs. The user can use the visualizations to get an idea of the sentiment distribution but can also dig deeper and look at the sentiment of particular tweets

Below I provide a more detailed explanation of the three modules used in this project as well as example outputs for each using "airpods" as the test product:

**1- twitter_api_module.py:**
This modules has two primrary functions. It extracts the tweets related to the specified product and number of tweets. It also cleans/preprocesses the data to prepare it for sentiment analysis.

Steps done to clean the tweets are as follows: 
 - Converting all letters to either upper case or lower case.
 - Stopword removal: Some words do not contribute much to the machine learning model, so it's good to remove them. A list of stopwords can be defined by the nltk library, or it can be business-specific.
 - Remove user @ references and '#' from tweet
 - Remove punctuations
 
An example of the output of this module is as follows for the product airpods: 
![alt text](https://github.com/mkhalil1998/EC-601-Twitter_Project/blob/main/Images/module1.png)

**2- google_api_module.py:**
This modules performs sentiment analysis on the tweets and according to the outputed score a sentiment level is provided for the tweet. It can be positive, neutral or negative. 

An example of the output of this module is as follows for the product airpods: 
![alt text](https://github.com/mkhalil1998/EC-601-Twitter_Project/blob/main/Images/module2.png)


**3- visualization_module.py:**
This model combines the results of the two previous models and tries to visualize the data. There are two types of visualizations. A pie chart showing the percentage of tweets per sentiment level, and a word cloud showing the most frequent words in the tweets. This is can provide insights on some key words. 

Pie chart: 
![alt text](https://github.com/mkhalil1998/EC-601-Twitter_Project/blob/main/Images/pie_chart.png)


Word Cloud: 
![alt text](https://github.com/mkhalil1998/EC-601-Twitter_Project/blob/main/Images/word_cloud.png)


## Project 3: Unit Tests for Twitter Project

**1 - (A) Google_NLP.py**
-------------------------
 
This is for defining a function to initalize google api, input document, 
and provide sentiment score for given text.

**1 - (B) test_Google_NLP.py**
-------------------------

I export the google api code and write a 
unit test to experiment with different inputs and test the output you would get

To run this python file: 
Type the sample text you want to text, change the assert function to the expected output 
and then run the test_Google_NLP.py file. 

**2 - (A) Twitter_API.py**
-------------------------

Defines two functions:
(1) authu, used to authenticate twitter api credentials
input: credentials
output: api 

(2) search_tweets, used to return most recent tweets for a specific query 
input: api, q(query), num_of_tweets
output: tweets and errors 

**2 - (B) Twitter_API.py**
-------------------------
 
Role of this test is to determine if the api search outputs something for the 
query. If it does then the assertion will hold and no errors will be printed. However, 
if it does not output anything then the assertion will fail and errors will be printed. 

This will allow us to test any input and see if an output or an error will be produced.

Example of test:
Test case description: Input numbers as query to twitter api
Test steps: Input a sequence of random numbers and record to see if the api is going 
        retrieve tweets or return an error
Test data: '94890'
Expected result: Return tweets contain this random number
Actual result: Returns tweets with random number




