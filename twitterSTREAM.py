import tweepy
import csv


class MyStreamListener(tweepy.StreamListener):
    # set up mongodb
    # mongo_setup.global_init()

    def on_status(self, status):
        screen_name = status.user.screen_name

        # filter for quote tweets
        if hasattr(status, 'quoted_status'):
            quote_tweet = status.quoted_status
            if hasattr(quote_tweet, 'user'):
                if quote_tweet.user is not None:
                    if hasattr(quote_tweet.user, screen_name):
                        if quote_tweet.user.screen_name is not None:
                            print(screen_name + " quote tweeted " + quote_tweet.user.screen_name)
                            print(status.text)
                            print("")

                            # save quote tweet information to CSV file
                            with open('twitterdata.csv', 'a') as file:
                                writer = csv.writer(file)
                                writer.writerow([status.text])

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

                            # save retweet information to CSV file
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

