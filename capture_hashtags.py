import csv

tweets = []
hashtags = []

with open('twitterdata.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        tweets.append(line[1])

for tweet in tweets:
    for word in tweet.split():
        if word[0] == "#" and word not in hashtags:
            if len(hashtags) == 0:
                hashtags.append(word)
            else:
                if word in hashtags[len(hashtags) -1] or hashtags[len(hashtags) -1] in word:
                    hashtags.append(word)

print(hashtags)

