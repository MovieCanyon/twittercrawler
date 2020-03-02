import csv
import tweepy


# actual crawler
def crawl(consumer_key, consumer_secret, access_token, access_token_secret):

    print("WE HAVE BEGUN!!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    hashtagSearch = '#coronavirus'
    maxTweets = 9000
    noOfTweets = 100
    file = 'twitterdata.csv'

    sinceId = None
    max_id = -1
    tweetCount = 0

    with open(file, 'a') as f:
        writer = csv.writer(f)
        while tweetCount < maxTweets:
            try:
                if max_id <= 0:
                    if not sinceId:
                        tweets = api.search(q=hashtagSearch, count=noOfTweets)
                    else:
                        tweets = api.search(q=hashtagSearch, count=noOfTweets, max_id=str(max_id - 1),
                                            since_id=sinceId)
                if not tweets:
                    print("NO NEW TWEETS")
                    break
                for tweet in tweets:
                    writer.writerow([tweet.text])
                    tweetCount += len(tweets)
                    max_id = tweets[-1].id
            except tweepy.TweepError as e:
                break
