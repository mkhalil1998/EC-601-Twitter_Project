# Importing libraries necessary for this module: 
# ----------------------------------------------
import Twitter_API
import pytest, sys

'''
Role of this test is to determine if the api search outputs something for the 
query. If it does then the assertion will hold and no errors will be printed. However, 
if it does not output anything then the assertion will fail and errors will be printed. 

This will allow us to test any input and see if an output or an error will be produced.

Example of test:
----------------
Test case description: Input numbers as query to twitter api
Test steps: Input a sequence of random numbers and record to see if the api is going 
        retrieve tweets or return an error
Test data: '94890'
Expected result: Return tweets contain this random number
Actual result: Returns tweets with random number
'''
# Function to print errors 
def print_errors(errors):
    print("Errors are: ")
    for statement in errors:
        print(statement)
    print('')

# Unit test
def test_twitter_api():
    api = Twitter_API.authu()
    (tweetList, errors) = Twitter_API.search_tweets(api, q='98490', num_of_tweets=10)
    assert (tweetList is not None)
    
    if tweetList is None:
        print_errors(errors)

if __name__ == '__main__':
    print("---------------")
    print('Performing Test')
    test_twitter_api()
    sys.exit(0)