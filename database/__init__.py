# needs for creating column, Foreignkey connect two key, but relationship bases
# create db ce
from sqlalchemy import create_engine
# sessionmaker connect to db
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connect to db
SQLALCHEMY_DATABASE_URI = "sqlite:///pay_test.db"
# connect_args= only for sqllite3
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False})

# session for db
SessionLocal = sessionmaker(bind=engine)

# common class for creating data model
Base = declarative_base()

# generation connect to db
def get_db():
    session = SessionLocal()
    try:
        yield session
    except:
        # if we get error during interaction with db rollback all changes and raise error
        session.rollback()
        raise
    finally:
        # close session in the end
        session.close()

# import functionality for db
from database.userservice import *
from database.cardservice import *
from database.businesservice import *
from database.paymentservice import *