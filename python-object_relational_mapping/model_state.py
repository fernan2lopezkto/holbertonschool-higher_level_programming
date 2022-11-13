#!/usr/bin/python3
''' documentation '''


""" imports"""
from sys import argv

from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine=('postgresql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
Base = declarative_base()

""" classss """
class State(Base):
    __tablename__ = "states"

    id = Column(Integer(), primary_key=True, auto_increment=True unique=True, nullable=False)
    name = Column(String(128), nullable=False)

Session = sessionmaker(engine)
sesion = Session()

if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)