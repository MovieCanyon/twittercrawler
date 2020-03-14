import twitterREST
import twitterSTREAM
import csv

# set up CSV file
with open('twitterdata.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow(["username", "tweet"])

# keys
consumer_key = #consumer_key goes here
consumer_secret = #consumer_secret goes here
access_token = #access_token goes here
access_token_secret = #access_token_secret goes here

twitterREST.crawl(consumer_key, consumer_secret, access_token, access_token_secret)
twitterSTREAM.crawl(consumer_key, consumer_secret, access_token, access_token_secret)


