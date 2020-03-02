import twitterREST
import twitterSTREAM
import csv

# set up CSV file
with open('twitterdata.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow(["tweet"])

# keys
consumer_key = 'hcJP7YDPGEF6Amsz4vqeVKs3y'
consumer_secret = '46p4RYkLzF2uPBx3Isvw2VAmu2FbfsxBLFvoZYFJIk0Bmu7X3h'
access_token = '2769456760-NLbQDpwwGYzWODWfAYniQY3kQqeNhlJw55hL3Ao'
access_token_secret = 'deiSH41U53vUgeKiEjOKPcGxDUqMm1GUEwlYYkwkLyzw7'

twitterREST.crawl(consumer_key, consumer_secret, access_token, access_token_secret)
#twitterSTREAM.crawl(consumer_key, consumer_secret, access_token, access_token_secret)


