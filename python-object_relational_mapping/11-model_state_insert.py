#!/usr/bin/python3
"""MODULE task 9"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from model_state import Base, State


Base = declarative_base()


if __name__ == '__main__':

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name = "Louisiana")
    session.add(louisiana)

    session.commit()

    result = session.query(State.id).filter(
        State.name.like("Louisiana")
    ).first()

    if result:
        print(result)
    else:
        print("Not found")

    session.close()
