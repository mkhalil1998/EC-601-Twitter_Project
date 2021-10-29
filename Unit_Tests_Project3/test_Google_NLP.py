import Google_NLP
import pytest
import sys

'''
I export the google api code and write a 
unit test to experiment with different inputs

To run this python file: 
Type the sample text you want to text, change the assert function to the expected output 
and then run the test_Google_NLP.py file. 

Output: Text and sentiment if assert function passes 
        or 
         Text and sentiment with error if it didnt pass 
'''

# Sample inputs:
# --------------
sample_text = 'I am okay'
sample_text2 = '%@*&#'
#sample_text = '93849'
#sample_text = 'I am very sad'
#sample_text = 'I am very happy'

# Function to print errors 
def print_errors(errors):
    print("Th errors are:")
    for statement in errors:
        print(statement)
    print('')

# Function to test different inputs to nlp 
def test_nlp():

    (sentimentDict,errors) = Google_NLP.analyze_sentiment(sample_text)
    (sentimentDict2,errors2) = Google_NLP.analyze_sentiment(sample_text2)

    assert (len(sentimentDict) != 0)
    assert (len(sentimentDict2) != 0)
    
    if len(sentimentDict) == 0 or len(sentimentDict2)== 0:
        print_errors(errors)
        print_errors(errors2)
        # Exiting system bcz of errors
        sys.exit(1)

    print('Text1: {}'.format(sample_text))
    print('Sentiment1: {}'.format(sentimentDict['score']))

    print('Text2: {}'.format(sample_text2))
    print('Sentiment2: {}'.format(sentimentDict2['score']))

    assert sentimentDict['score'] == pytest.approx(0.5,1)
    assert sentimentDict2['score'] == pytest.approx(-0.3,1)

if __name__ == '__main__':
    test_nlp()