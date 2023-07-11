from fastapi import FastAPI
from database import Base, engine

# create tables for db
Base.metadata.create_all(bind=engine)


app = FastAPI()
from business import business_api
from card_management_transfer import card_api
from user_authentication import user_api

@app.get('/')
async def test_fast():
    return 'Hello'

