from fastapi import FastAPI

from schemas import Joke

app = FastAPI()


@app.post('/joke')
def create_joke(item: Joke):
    return item


@app.get('/joke')
def get_joke(q: str = 'test'):
    return q


@app.get('/joke/{pk}')
def get_single_joke(pk: int):
    return {"pk": pk}
