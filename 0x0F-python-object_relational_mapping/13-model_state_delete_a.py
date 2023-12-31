#!/usr/bin/python3
"""script changes the name of a State obj from the database
hbtn_0e_6_usa"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(username,
                                password,
                                database_name),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    query = session.query(State).filter(State.name.like('%a%'))
    for row in query:
        session.delete(row)
    session.commit()
    session.close()
