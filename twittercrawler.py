import tweepy
import mongo_setup
import quotetweet
import retweets
import csv
import extract_keywords, extract_hashtags

# list of hashtags to looks for it tweets
hashtags = ['#happy', '#sad', '#excited', '#angry', '#disgusted', '#surprised']


class MyStreamListener(tweepy.StreamListener):

    # set up mongodb
    mongo_setup.global_init()

    # set up CSV file
    with open('twitterdata.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(["user", "retweeted/quoted user", "tweet"])

    def on_status(self, status):
        screen_name = status.user.screen_name

        # group each individual keyword in a separate csv file
        if "cornoavirus" in status.text:
            extract_keywords.extract_cornonavirus(status.text, screen_name)
        elif "python" in status.text:
            extract_keywords.extract_python(status.text, screen_name)
        elif "movies" in status.text:
            extract_keywords.extract_movies(status.text, screen_name)

        # group tweets with the specific hashtags we're looking for in a separate csv file
        for hashtag in hashtags:
            if hashtag in status.text:
                extract_hashtags.extract_hashtag_information(status.text, screen_name)

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

                            # save quote tweet information to mongoDB
                            quotetweet_instance = quotetweet.QuoteTweet

                            quotetweet_instance.user = screen_name
                            quotetweet_instance.quotedUser = quote_tweet.user.screen_name
                            quotetweet_instance.tweet = status.text

                            # save quote tweet information to CSV file
                            with open('twitterdata.csv', 'a') as file:
                                writer = csv.writer(file)
                                writer.writerow([screen_name, quote_tweet.user.screen_name, status.text])

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

                            # save retweet information to mongoDB
                            retweet_instance = retweets.Retweets
                            retweet_instance.user = screen_name
                            retweet_instance.retweetedUser = retweet.user.screen_name
                            retweet_instance.tweet = status.text

                            # save retweet information to CSV file
                            with open('twitterdata.csv', 'a') as file:
                                writer = csv.writer(file)
                                writer.writerow([screen_name, retweet.user.screen_name, status.text])


# actual crawler
def crawl(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    # filter for tweets in english, track words 'python', 'coronavirus' and 'movies'
    myStream.filter(languages=["en"], track=['python', 'coronavirus', 'movies'])


# keys
consumer_key = 'hcJP7YDPGEF6Amsz4vqeVKs3y'
consumer_secret = '46p4RYkLzF2uPBx3Isvw2VAmu2FbfsxBLFvoZYFJIk0Bmu7X3h'
access_token = '2769456760-NLbQDpwwGYzWODWfAYniQY3kQqeNhlJw55hL3Ao'
access_token_secret = 'deiSH41U53vUgeKiEjOKPcGxDUqMm1GUEwlYYkwkLyzw7'

if __name__ == '__main__':
    crawl(consumer_key, consumer_secret, access_token, access_token_secret)
