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

# Function to print errors 
def print_errors(errors):
    print("The errors are:")
    for statement in errors:
        print(statement)
    print('')

# Function to test positive sentiment different inputs to nlp 
def test_positive_sentiment():
    (sentimentDict,errors) = Google_NLP.analyze_sentiment("I am really happy today") 
    assert(len(sentimentDict) != 0)
    assert(round(sentimentDict['score']) == 1)

    if len(sentimentDict) == 0:
        print_errors(errors)

    return

# Function to test Negative sentiment different inputs to nlp 
def test_negative_sentiment():
    (sentimentDict,errors) = Google_NLP.analyze_sentiment("I am really sad today") 
    assert(len(sentimentDict) != 0)
    assert(round(sentimentDict['score']) == -1)

    if len(sentimentDict) == 0:
        print_errors(errors)

    return

# Function to test unusual input
def test_unusual_sentiment():
    (sentimentDict,errors) = Google_NLP.analyze_sentiment("$#^*@") 
    assert(len(sentimentDict) != 0)
    assert(round(sentimentDict['score']) == pytest.approx(-0.3,1))

    if len(sentimentDict) == 0:
        print_errors(errors)

    return


if __name__ == '__main__':
    test_positive_sentiment()
    test_negative_sentiment()
    test_unusual_sentiment()