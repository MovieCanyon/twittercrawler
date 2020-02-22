import mongoengine


class QuoteTweet(mongoengine.Document):
    tweet = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'quote_tweet'
    }