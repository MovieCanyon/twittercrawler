import tweepy
import csv


# StreamListener
class MyStreamListener(tweepy.StreamListener):
    # set up mongodb
    # mongo_setup.global_init()

    def on_status(self, status):
        print(status.text)

        # save tweet information to CSV file
        with open('twitterdata.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([status.text])


# actual crawler
def crawl(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    # filter for tweets in english, track words 'python', 'coronavirus' and 'movies'
    myStream.filter(languages=["en"], track=['python', 'coronavirus', 'movies'])
