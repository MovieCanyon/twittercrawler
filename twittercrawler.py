import tweepy
import mongo_setup
import tweepy
import mongo_setup


class MyStreamListener(tweepy.StreamListener):
    # set up mongodb
    mongo_setup.global_init()

    def on_status(self, status):
        screen_name = status.user.screen_name

        # filter for quote tweets
        if hasattr(status, 'quoted_status'):
            quote = status.quoted_status
            if 'user' in quote:
                if quote['user'] is not None:
                    if "screen_name" in quote['user']:
                        if quote['user']['screen_name'] is not None:
                            print(screen_name + " quote tweeted " + quote['user']['screen_name'])
                            print(status.text)
                            print("")

        # filter for retweets
        if hasattr(status, 'retweeted_status'):
            retweet = status.retweeted_status
            if hasattr(retweet, 'user'):
                if retweet.user is not None:
                    if hasattr(retweet.user, 'screen_name'):
                        if retweet.user.screen_name is not None:
                            print(screen_name + " retweeted " + retweet.user.screen_name)
                            print(status.text)
                            print("")

# actual crawler
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
