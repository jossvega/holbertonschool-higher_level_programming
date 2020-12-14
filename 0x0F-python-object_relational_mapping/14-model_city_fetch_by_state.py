#!/usr/bin/python3
"""
Write a Python file similar to model_state.py
named model_city.py that contains the class
definition of a City
"""


if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@192.168.1.55/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    for state, city in session.query(State, City)\
                              .filter(City.state_id == State.id)\
                              .order_by(City.id).all():
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
