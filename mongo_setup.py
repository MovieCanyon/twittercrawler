import pymongo


def global_init():

    client = pymongo.MongoClient('127.0.0.1', 27017)
    print(client.list_database_names())
    db = client.twitterStream
    db1 = client.twitterDump
    dbl = client.Logs
    db3 = client.invertedIndex

    print(db.collection.stats())
