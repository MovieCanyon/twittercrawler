import csv

# read in csv data
# extract all the usernames
# go through each username and create dictionary of frequency
# do for regular tweets, then retweets, then quote tweets

# Example: {'A': {'B': 3, 'C': 4}, 'B': {'C': 1}, 'C': {'B': 3, 'D': 2}}

user_dict = {}
user_dict_retweet = {}
user_dict_quote = {}

with open('twitterdata.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        if line[0] not in user_dict:
            user_dict[line[0]] = {}

        # build dictionary for general tweet information
        tweet_text = line[1].split(" ")
        for text in tweet_text:
            if text != "" and text[0] == "@":
                if text in user_dict[line[0]]:
                    user_dict[line[0]][text] = user_dict[line[0]][text] + 1
                else:
                    user_dict[line[0]][text] = 1

        # build dictionary for retweets
        if tweet_text[0] == "RT":

            if line[0] not in user_dict_retweet:
                user_dict_retweet[line[0]] = {}

            for text in tweet_text:
                if text != "" and text[0] == "@":
                    if text in user_dict_retweet[line[0]]:
                        user_dict_retweet[line[0]][text] = user_dict_retweet[line[0]][text] + 1
                    else:
                        user_dict_retweet[line[0]][text] = 1

        # build dictionary for quote tweets
        if tweet_text[0] == "QT":

            if line[0] not in user_dict_quote:
                user_dict_quote[line[0]] = {}

            for text in tweet_text:
                if text != "" and text[0] == "@":
                    if text in user_dict_quote[line[0]]:
                        user_dict_quote[line[0]][text] = user_dict_quote[line[0]][text] + 1
                    else:
                        user_dict_quote[line[0]][text] = 1


def print_general_network():
    print("")
    print("General Tweet Network:")
    print("")
    print(user_dict)


def print_retweet_network():
    print("")
    print("Retweet Network:")
    print("")
    print(user_dict_retweet)


def print_quote_network():
    print("")
    print("Quote Tweet Network:")
    print("")
    print(user_dict_quote)
