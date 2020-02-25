import mongoengine


class Retweets(mongoengine.Document):
    user = mongoengine.StringField(required=True)
    retweetedUser = mongoengine.StringField(required=True)
    tweet = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'retweets'
    }
