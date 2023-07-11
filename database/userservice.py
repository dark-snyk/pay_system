from database.models import User, Password
from database import get_db

# user registration, qwargs pass dict
def register_user_db(**kwargs):
    # phone number is a key of dict value
    db = next(get_db())
    phone_number = kwargs.get('phone_number')

    # check phone number
    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        return "user already exists in db"

    # if not exists, proceed registration
    new_user = User(**kwargs)
    db.add(new_user)
    db.commit()

    # create password for new_user
    new_user_password = Password(user_id=new_user.user_id, **kwargs)
    db.add(new_user_password)
    db.commit()

    return "user added to db"

def check_password_db(phone_number, password):
    db = next(get_db())
    checker = db.query(Password).filter_by(phone_number=phone_number).first()

    if checker and checker.password == password:
        return checker.user_id
    elif not checker:
        return "error in number"
    elif checker.password != password:
        return "something get wrong"

# getting information
def get_user_cabinet_db(user_id):
    db = next(get_db())

    checker = db.query(User).filter_by(user_id=user_id).first()
    if checker:
        return checker
    return "data error"
