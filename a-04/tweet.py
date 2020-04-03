from twython import Twython
import socket
import time

# generated credentials from Twitter API
CONSUMER_KEY = 'my_consumer_key'
CONSUMER_SECRET = 'my_consumer_secret'
TOKEN_KEY = 'my_token_key'
TOKEN_SECRET = 'my_token_secret'


def post_tweet():
    # form an unique tweet (cannot tweet the same text twice)
    tweet_text = '#iotupt {0} started assignment at {1}'.format(socket.gethostname(), time.strftime('%H:%M:%S'))
    # build twython object based on supplied credentials
    twitter_api = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN_KEY, TOKEN_SECRET)
    # update twitter status ~ post a tweet
    twitter_api.update_status(status=tweet_text)
    # log posted message for easy tracking
    print('posted: ', tweet_text)


# tweet once
post_tweet()
