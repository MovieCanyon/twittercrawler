import csv


def extract_hashtag_information(tweet, user):
    with open('hashtag_tweets.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([user, tweet])
