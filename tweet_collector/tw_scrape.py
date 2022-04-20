import tweepy
import logging
from pymongo import MongoClient
from credentials import BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET # storage for authentification

# authentication
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       wait_on_rate_limit=True)

# establish connection with mongodb
conn = MongoClient('mongomongodb')

# search tweets based on keywords
search_query = '(chickenrice OR "chicken rice") -is:retweet -is:reply -is:quote lang:en'

cursor = tweepy.Paginator(
    method=client.search_recent_tweets,
    query=search_query,
    tweet_fields=['author_id', 'created_at', 'public_metrics', 'source','attachments','geo'],
    expansions=['attachments.media_keys']
).flatten(limit=200)

# create tweet_collector database
db = conn.tweet_collector
tweet_collection = db.tweets

for t in cursor:
    tweet_collection.insert_one(dict(t))
    print(t)
# try with one tweet
