import tweepy
from textblob import TextBlob
import config as cfg
import numpy as np

auth = tweepy.OAuthHandler(cfg.API_KEY, cfg.API_SECRET_KEY)
auth.set_access_token(cfg.ACCESS_TOKEN, cfg.ACCESS_SECRET_TOKEN)

api = tweepy.API(auth)


def get_analysis(topic):
    tweets = api.search_tweets(topic)
    sentiment = [TextBlob(tweet.text).sentiment for tweet in tweets]
    try:
        avg_subjectivity = np.array([s.subjectivity for s in sentiment if s.subjectivity != 0]).mean()
        avg_polarity = np.array([s.polarity for s in sentiment if s.polarity != 0]).mean()
    except Exception as e:
        print(e)
    return avg_polarity, avg_subjectivity
