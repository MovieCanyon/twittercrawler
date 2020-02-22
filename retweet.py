import mongoengine

class Retweets(mongoengine.Document):
    tweet = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'retweets'
    }

