import csv


def extract_python(tweet, user):
    with open('python_tweets.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([user, tweet])


def extract_cornonavirus(tweet, user):
    with open('corona_tweets.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([user, tweet])


def extract_movies(tweet, user):
    with open('movie_tweets.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([user, tweet])
