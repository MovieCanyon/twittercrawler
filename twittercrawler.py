import json
from typing import Dict, Any
import tweepy
import re


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


def crawl(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    myStream.filter(track=['python'])


consumer_key = 'hcJP7YDPGEF6Amsz4vqeVKs3y'
consumer_secret = '46p4RYkLzF2uPBx3Isvw2VAmu2FbfsxBLFvoZYFJIk0Bmu7X3h'
access_token = '2769456760-NLbQDpwwGYzWODWfAYniQY3kQqeNhlJw55hL3Ao'
access_token_secret = 'deiSH41U53vUgeKiEjOKPcGxDUqMm1GUEwlYYkwkLyzw7'

if __name__ == '__main__':
    crawl(consumer_key, consumer_secret, access_token, access_token_secret)
