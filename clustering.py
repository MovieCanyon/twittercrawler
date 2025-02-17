import csv
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

# open test data from csv file into array
data = []
users = []
hashtags = []

with open('twitterdata.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        if line[1].split(" ")[0] != "RT":
            if line[1].split(" ")[0] == "QT":
                data.append(line[1][6:])
            else:
                data.append(line[1])

for tweet in data:
    for word in tweet.split():
        if word[0] == '@':
            users.append(word)
        elif word[0] == '#':
            hashtags.append(word)

# perform clustering on the text
vectoriser = TfidfVectorizer()
X = vectoriser.fit_transform(data)
k = 10
model = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
print("")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectoriser.get_feature_names()
for i in range(k):
    print("Cluster %d:" % i)
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])
    print("")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# perform clustering on users
vectoriser = TfidfVectorizer()
X = vectoriser.fit_transform(users)
k = 10
model = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top users per cluster:")
print("")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectoriser.get_feature_names()
for i in range(k):
    print("Cluster %d:" % i)
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])
    print("")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# perform clustering on hashtags
vectoriser = TfidfVectorizer()
X = vectoriser.fit_transform(hashtags)
k = 10
model = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top hashtags per cluster:")
print("")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectoriser.get_feature_names()
for i in range(k):
    print("Cluster %d:" % i)
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])
    print("")