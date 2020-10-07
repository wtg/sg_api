from dataclasses import dataclass
from typing import Dict, Optional

from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}


@dataclass
class Item:
    item_id: int
    q: Optional[str]


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None) -> Item:
    return Item(item_id, q)
