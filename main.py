from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: int):  # localhost/items/10/?q=5 -> query
    return {"item_id": item_id, "q": q}
