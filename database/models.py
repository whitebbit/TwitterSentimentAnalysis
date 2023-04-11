import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import sqltypes as types
from sqlalchemy import Column, create_engine
from sqlalchemy_utils import database_exists

import database


def initialize():
    engine = create_engine(database.url)
    if database_exists(database.url):
        return
    database.Base.metadata.create_all(engine)


class SentimentTweets(database.Base):
    __tablename__ = "sentimenttweets"

    id = Column(types.Integer, primary_key=True)
    topic = Column(types.String)
    avg_polarity = Column(types.FLOAT)
    avg_subjectivity = Column(types.FLOAT)

    def __repr__(self):
        return f"{self.id} | {self.tweet} | {self.avg_sentiment}"


initialize()
