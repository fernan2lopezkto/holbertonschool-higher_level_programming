#!/usr/bin/python3
"""list all states """

from model_state import Base, State
from sys import argv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2],argv[3]),)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    result = session.query(State).all()

    for item in result:
        print('{}: {}'.format(item.id, item.name))

    session.close()