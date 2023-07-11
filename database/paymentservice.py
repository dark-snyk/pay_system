from database.models import Service, Transaction, Card
from database import get_db

def transfer_money_db(card_from, card_to, date, amount):
    db = next(get_db())

    card_from_checker = get_exact_card_balance_db(card_from)
    card_to_checker = get_exact_card_balance_db(card_to)

    if (card_from_checker and card_to_checker) and (card_from_checker.balance >= amount):
        transaction = Transaction(card_to=card_to, card_id=card_from_checker.card_id, amount=amount)

        card_from_checker.balance -= amount
        card_to_checker.balance += amount

        db.add(transaction)
        db.commit()
        return "transfer success"
    elif not card_to_checker or not card_from_checker:
        return "data error"
    else:
        return "not enough balance"

def pay_for_service_db(from_card: int, amount: float, business_id: int):
    db = next(get_db())
    # check balance
    checker = get_exact_card_balance_db(from_card)
    if checker.balance >= amount:
        transaction = Transaction(card_to=business_id, card_id=checker.card_id, amount=amount)

        checker.balance -= amount
        db.add(transaction)
        db.commit()
        return "service payd"
    elif not checker:
        return "error data"
    else:
        return "not enough money"


# get balance exact card
def get_exact_card_balance_db(card_number):
    db = next(get_db())

    exact_card = db.query(Card).filter_by(card_number=card_number).first()
    return exact_card