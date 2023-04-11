from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import database
from database.models import SentimentTweets


def add(session, topic, polarity, subjectivity):
    if topic_exist(session, topic.title()):
        raise ValueError("Value exist")

    item = SentimentTweets(topic=topic.title(), avg_polarity=polarity, avg_subjectivity=subjectivity)
    session.add(item)
    session.commit()


def delete(session, topic):
    item = session.query(SentimentTweets).filter(SentimentTweets.topic == topic).first()
    session.delete(item)
    session.commit()


def get(session, topic):
    item = session.query(SentimentTweets).filter(SentimentTweets.topic == topic).first()
    return item


def topic_exist(session, topic):
    return get(session, topic) is not None


def all_items(session):
    for item in session.query(SentimentTweets).all():
        yield item
