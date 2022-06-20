from typing import List

from fastapi import FastAPI, Query
from schemas import Book


app = FastAPI()


@app.get('/')
def home():
    return {"key": "Hello"}


# @app.get('/{pk}')
# def get_item(pk: int, q: int = None):
#     return {"key": pk, "q": q}
#
#
# @app.get('/user/{pk}/items/{item}/')
# def get_user_item(pk: int, item: str):
#     return {"key": pk, "item": item}


@app.post('/book')
def create_book(item: Book):
    return item


@app.get('/book')
def get_book(q: List[str] = Query("test", description="Search book", deprecated=True)):
    return q
