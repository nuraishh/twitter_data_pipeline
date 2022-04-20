import pymongo
from pymongo import MongoClient
import sqlalchemy
from sqlalchemy import create_engine
import time
from time import sleep
import numpy
from numpy import random
import pandas as pd
import logging

# establish connection with mongodb
conn_string_mdb = f"mongodb://mongomongodb:27017"
client = MongoClient(conn_string_mdb)

# selecting database (used in tw_scrape)
db = client.tweet_collector

# connecting to the collection 'tweet_collection'
tweet_collection = db.tweets

# sanity check
docs = db.tweets.find()
for doc in docs:
    print(doc)

# let chill to let mongodb restart
time.sleep(10)

# postgres
# establish connection with postgresql
conn_string_pg = f"postgresql://postgres:postgres@postgrespostgresdb:5432/tweet_collector"
pg = create_engine(conn_string_pg)


# create table
pg.execute("""
CREATE TABLE IF NOT EXISTS tweet_table (
    id NUMERIC,
    text VARCHAR(500),
    sentiment TEXT
);

""")

# insert into postgresql
for doc in docs:
    text = doc['text']
    score = 1.0  # placeholder value
    query = "INSERT INTO tweet_table VALUES (%s, %s);"
    pg.execute(query, (text, score))
