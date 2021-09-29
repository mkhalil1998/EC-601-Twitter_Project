# EC-601-Twitter_Project

Phase 1 a: Exploring the twitter API
--------

TwitterProject-Phase1.py allows the user to extract the most recent twitter posts for a particular user. 
The code also cleans the data so that it is ready for the next step of NLP. 

Testing: The code was tested with extracting the most recent twitter posts from Cristiano Ronaldo and they were compared to the tweets on twitter.


Phase 1 b: Exploring the Google NLP API 
--------

TwitterProject-Phase1b.py allows the user to use the extracted text from twitter that can be done using TwitterProject-Phase1.py and input it to the new function entiment_analysis_tweets. According to the generated sentiment score, the tweet is categorized into one of the sentiment levels. 
 
 - 0.7 - 1 -> Very Positive 
 - 0.3 - 0.7 -> Positive 
 - 0.3 - -0.3 -> OK 
 - -0.3 - -1 -> Negative 
 
Testing: The code was tested with extracting the 10 most recent twitter posts from the White House and each post was given a sentiment level. 
