from pydantic import BaseModel


class Joke(BaseModel):
    id: int
    text: str
    rating: str
