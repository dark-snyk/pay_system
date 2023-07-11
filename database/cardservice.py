from database.models import Card, User, Transaction
from database import get_db

# add card to db
def add_user_card_db(**kwargs):
    db = next(get_db())
    card_number = kwargs.get('card_number')

    # check if card exists
    checker = db.query(Card).filter_by(card_number=card_number).first()

    if checker:
        return "card exists in db"
    new_card = Card(**kwargs)
    db.add(new_card)
    db.commit()

    return "card added succesfuly"


# make transfer from card to card
def transfer_money_db(card_from, card_to, date):
    pass

# delete card from service
def delete_user_card_db(card_id, user_id):
    db = next(get_db())
    exact_card = db.query(Card).filter_by(card_id=card_id).first()

    if exact_card:
        db.delete(exact_card)
        db.commit()
        return "card successfuly deleted"
    return "data error"


# get all card by phone number
def get_user_cards_by_phone_number_db(phone_number):
    db = next(get_db())
    checker = db.query(Card).filter(User.phone_number==phone_number).all()
    return checker

# get exact info
def get_exact_user_card_db(user_id, card_id):
    db = next(get_db())
    if card_id == 0:
        card_data = db.query(Card).filter_by(user_id=user_id).all()

    else:
        card_data = db.query(Card).filter_by(user_id=user_id, card_id=card_id).first()
    return card_data

# get all transactions by exact cards
def get_all_cards_or_exact_transactions(user_id, card_id):
    db = next(get_db())
    if card_id == 0:
        card_monitor = db.query(Transaction).filter_by(user_id=user_id).all()

    else:
        card_monitor = db.query(Transaction).filter_by(user_id=user_id, card_id=card_id)
    return card_monitor