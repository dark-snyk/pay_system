from database.models import Transaction, ServiceCategory, Service
from database import get_db


# registration business by category
def register_business_category_db(name: str):
    db = next(get_db())

    new_category = ServiceCategory(name=name)

    db.add(new_category)
    db.commit()

    return "business successfully registered"


# registration business
def register_business_db(category_id: int, name: str, card_number: int):
    db = next(get_db())

    new_business = Service(category_id=category_id,
                           name=name,
                           service_check=card_number)
    db.add(new_business)
    db.commit()

    return "business successfully registered"


# output all categories
def get_business_categories_db(exact_category_id: int = 0):
    db = next(get_db())

    if exact_category_id == 0:
        categories = db.query(ServiceCategory).all()
    else:
        categories = db.query(ServiceCategory).filter_by(id=exact_category_id).all()

    return categories


# output service
def get_exact_business_db(business_id: int, category_id: int):
    db = next(get_db())

    business = db.query(Service).filter_by(id=business_id,
                                           category_id=category_id).first()
    if business:
        return business
    else:
        return "business not found"


# delete business
def delete_business_db(business_id: int):
    db = next(get_db())

    business = db.query(Service).filter_by(service_id=business_id).first()

    if business:
        db.delete(business)
        db.commit()

        return "business successfully deleted"
    else:
        return "business not found"


# delete business category
def delete_business_category_db(category_id: int):
    db = next(get_db())

    category = db.query(Service).filter_by(category_id=category_id).first()

    if category:
        db.delete(category)
        db.commit()
        return "business successfully deleted"
    else:
        return "business not found"
