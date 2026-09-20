from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

app = FastAPI(title="Item API")

frontend_dir = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=str(frontend_dir)), name="static")


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., ge=0)


class ItemPublic(BaseModel):
    id: int
    name: str
    price: float


_items: list[ItemPublic] = []
_next_id = 0


def _find(item_id: int) -> ItemPublic | None:
    for item in _items:
        if item.id == item_id:
            return item
    return None


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/items", response_model=list[ItemPublic])
def read_items(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, ge=1, description="Maximum number of items to return"),
    q: str | None = Query(None, description="Query string for searching items"),
):
    filtered_items = _items
    if q:
        filtered_items = [item for item in filtered_items if q.lower() in item.name.lower()]
    return filtered_items[skip: skip + limit]


@app.get("/items/{item_id}", response_model=ItemPublic)
def get_item(item_id: int):
    item = _find(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", response_model=ItemPublic, status_code=201)
def create_item(item: ItemCreate):
    global _next_id

    new_item = ItemPublic(
        id=_next_id,
        name=item.name,
        price=item.price,
    )
    _items.append(new_item)
    _next_id += 1
    return new_item


@app.put("/items/{item_id}", response_model=ItemPublic)
def update_item(item_id: int, data: ItemCreate):
    item = _find(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    updated_item = ItemPublic(
        id=item.id,
        name=data.name,
        price=data.price,
    )
    index = _items.index(item)
    _items[index] = updated_item
    return updated_item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    item = _find(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    _items.remove(item)
    return None