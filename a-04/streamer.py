from twython import TwythonStreamer
import pprint


# generated credentials from Twitter API
CONSUMER_KEY = 'my_consumer_key'
CONSUMER_SECRET = 'my_consumer_secret'
TOKEN_KEY = 'my_token_key'
TOKEN_SECRET = 'my_token_secret'


class NearbyTwythonStreamer(TwythonStreamer):

    def __init__(self, nearby, api_key, api_secret, token_key, token_secret):
        super(NearbyTwythonStreamer, self).__init__(app_key=api_key,
                                                    app_secret=api_secret,
                                                    oauth_token=token_key,
                                                    oauth_token_secret=token_secret)
        self.nearby = nearby

    def on_success(self, data):
        if 'text' in data:
            print('new post: {0}'.format(str(data['text'])))

    def on_error(self, status_code, data):
        print('{0}:{1}'.format(str(status_code), pprint.pprint(data)))

    def find_nearby(self):
        self.statuses.filter(track=self.nearby)


def listen_stream(keyword):
    streamer = NearbyTwythonStreamer(keyword,
                                     CONSUMER_KEY,
                                     CONSUMER_SECRET,
                                     TOKEN_KEY,
                                     TOKEN_SECRET)
    streamer.find_nearby()



hashtag = '#iotupt'
listen_stream(hashtag)
