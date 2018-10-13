

# Import the necessary methods from "twitter" library
# from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
#
# ACCESS_TOKEN = '15811365-Yu778Yf3icga9ox9kHC4S6yRVM6wA54h5tflSPOPC'
# ACCESS_SECRET = '4BeoHmqwmPiwDkk9ivcxoG7uany42yh6lMD6rNOTGdCr8'
# CONSUMER_KEY = 'z6rEESS0ZGf54bmBgx7dD04re'
# CONSUMER_SECRET = 'mtsFEbNapWBovK4BX5tHI5ZkaZQYEvMIjUqxHoXyVIo4gdNCQQ'
#
# oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
#
# # Initiate the connection to Twitter Streaming API
# twitter_stream = TwitterStream(auth=oauth)
#
# # Get a sample of the public data following through Twitter
# iterator = twitter_stream.statuses.sample()


import tweepy
import pandas as pd
from pandas.io.json import json_normalize

# Consumer keys and access tokens, used for OAuth
consumer_key = 'z6rEESS0ZGf54bmBgx7dD04re'
consumer_secret = 'mtsFEbNapWBovK4BX5tHI5ZkaZQYEvMIjUqxHoXyVIo4gdNCQQ'
access_token = '15811365-Yu778Yf3icga9ox9kHC4S6yRVM6wA54h5tflSPOPC'
access_token_secret = '4BeoHmqwmPiwDkk9ivcxoG7uany42yh6lMD6rNOTGdCr8'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

df = pd.DataFrame()

for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump', include_rts=True).items():
    # print(status._json['text'])
    if df.empty:
        df = json_normalize(status._json)
        df = df[['created_at', 'text']]
        df.to_csv('white_house_tweet_data.csv', index = False)
    else:
        new = json_normalize(status._json)
        tweet_date = new['created_at'].values[0]
        print(tweet_date)
        new = new[['created_at', 'text']]
        with open('white_house_tweet_data.csv', 'a') as f:
            new.to_csv(f, header=False, index=False)
