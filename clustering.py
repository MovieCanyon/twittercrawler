import csv
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

# open test data from csv file into array
data = []
with open('twitterdata.csv', 'r') as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        line = line[0]
        data.append(line)

# perform clustering on the text

vectoriser = TfidfVectorizer(stop_words='english')
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


