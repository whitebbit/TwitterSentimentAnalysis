from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import URL, create_engine

url = URL.create(
    drivername="sqlite",
    database="sentimenttweets.db"
)

Base = declarative_base()




