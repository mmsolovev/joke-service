from fastapi import FastAPI

from schemas import Joke

app = FastAPI()


@app.get('/')
def get_joke(q: Joke):
    return q
