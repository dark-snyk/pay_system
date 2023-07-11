from database import Base
from sqlalchemy import Column, String, Integer, Boolean, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

# users table
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    phone_number = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    reg_date = Column(DateTime)


# cards table
class Card(Base):
    __tablename__ = 'user_cards'
    card_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    card_number = Column(Integer, nullable=False)
    card_name = Column(String)
    cardholder = Column(String)
    exp_date = Column(Integer, nullable=False)
    added_date = Column(DateTime)
    balance = Column(Float)

    user_fk = relationship(User)

# payments table
class Transaction(Base):
    __tablename__ = 'user_transaction'
    transaction_id = Column(Integer, autoincrement=True, primary_key=True)
    card_id = Column(Integer, ForeignKey("user_cards.card_id"), nullable=False)
    amount = Column(Float, nullable=False)
    card_to = Column(Integer, nullable=False)
    transaction_date = Column(DateTime)

    card_fk = relationship(Card)

# services  table
class ServiceCategory(Base):
    __tablename__ = 'service_categories'
    category_id = Column(Integer, autoincrement=True, primary_key=True)
    category_name = Column(String, nullable=False)
    added_date = Column(DateTime)


class Service(Base):
    __tablename__ = 'services'
    service_id = Column(Integer, autoincrement=True, primary_key=True)
    service_category = Column(Integer, ForeignKey('service_categories.category_id'), nullable=False)
    service_name = Column(String, nullable=False)
    service_balance= Column(Float)
    service_check = Column(Integer, nullable=False)
    reg_date = Column(DateTime)

    category_fk = relationship(ServiceCategory)


# password table
class Password(Base):
    __tablename__ = 'user_password'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    password = Column(String, nullable=False)
    pincode = Column(Integer)

    # link to all User info
    user_fk = relationship(User)