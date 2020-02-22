import mongoengine


class QuoteTweet(mongoengine.Document):
    user = mongoengine.StringField(required=True)
    quotedUser = mongoengine.StringField(required=True)
    tweet = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'quote_tweet'
    }
