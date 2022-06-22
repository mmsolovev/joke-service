from pydantic import BaseModel
from datetime import date


class Joke(BaseModel):
    id: int
    text: str
    author: str
    date: date
    rating: str
