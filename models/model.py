from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Teams(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    team_name = Column(String)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email_id = Column(String, unique=True)
