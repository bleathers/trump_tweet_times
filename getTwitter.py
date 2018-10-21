import tweepy
import pandas as pd
from pandas.io.json import json_normalize

# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

df = pd.DataFrame()

for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump', include_rts=True).items():
    # print(status._json['text'])
    if df.empty:
        json_normalize(status._json)[['created_at', 'text']].to_csv('white_house_tweet_data.csv', index = False)
    else:
        new = json_normalize(status._json)[['created_at', 'text']]
        print(new['created_at'].values[0])
        with open('white_house_tweet_data.csv', 'a') as f:
            new.to_csv(f, header=False, index=False)
