# Importing libraries necessary for this module: 
# ----------------------------------------------
from google.cloud import language_v1
import os   

'''
This is for defining a function to initalize google api, input document, 
and provide sentiment score for given text.
Note: path to json google_api credentials should be set before running file 

    input: text 
    output: sentiment score if input is valid and error is none 
            or 
            sentiment is none and error for reason 
'''


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= ""
client = language_v1.LanguageServiceClient()

def analyze_sentiment(text):
    sentiment_d = {}
    sentiment = None
    errors = []
    try:
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        
    except:
        errors.append(analyze_sentiment.__name__ + ': Error with analyzing text sentiment')

    if sentiment is not None:
        sentiment_d = {"score":sentiment.score}
    
    return (sentiment_d,errors)