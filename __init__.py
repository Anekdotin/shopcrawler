from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI_0


# engine 1
engine = create_engine(SQLALCHEMY_DATABASE_URI_0)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

