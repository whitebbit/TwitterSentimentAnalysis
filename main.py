import tweepy
from textblob import TextBlob
import config as cfg

auth = tweepy.OAuthHandler(cfg.API_KEY, cfg.API_SECRET_KEY)
auth.set_access_token(cfg.ACCESS_TOKEN, cfg.ACCESS_SECRET_TOKEN)

api = tweepy.API(auth)


def get_analysis(topic):
    tweets = api.search_tweets(topic)
    analysis = [TextBlob(tweet.text).sentiment for tweet in tweets]
    return analysis

