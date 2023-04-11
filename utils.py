from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
import database
from sentiment_analysis import get_analysis
from database import utils as db
import matplotlib.pyplot as plt


def add_data(topic):
    engine = create_engine(database.url)
    session = sessionmaker(bind=engine)()
    polarity, subjectivity = get_analysis(topic)
    db.add(session, topic, polarity, subjectivity)


def get_polarity_graph(type_=None):
    engine = create_engine(database.url)
    df = pd.read_sql("SELECT * FROM sentimenttweets", engine)

    types = {
        None: df,
        "Negative": df[(df["avg_polarity"] < df["avg_polarity"].mean())],
        "Positive": df[(df["avg_polarity"] > df["avg_polarity"].mean())]
    }
    topics = [t[1] for t in types[type_].values]
    polarity = [t[2] for t in types[type_].values]
    plt.bar(topics, polarity)

    plt.xlabel('Topic Name')
    plt.ylabel('Polarity Value')

    plt.show()


def get_most_significant():
    engine = create_engine(database.url)
    df = pd.read_sql("SELECT * FROM sentimenttweets", engine)
    high = df[df["avg_polarity"] == df["avg_polarity"].max()]
    low = df[df["avg_polarity"] == df["avg_polarity"].min()]
    values = [*high.values, *low.values]
    topics = [t[1] for t in values]
    polarity = [t[2] for t in values]
    plt.bar(topics, polarity)

    plt.xlabel('Topic Name')
    plt.ylabel('Polarity Value')

    plt.show()
