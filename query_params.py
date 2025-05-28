from fastapi import FastAPI

app = FastAPI()

fake_items_db:list[dict[str, str]] = [{"item_id":1},{"item_id":2},{"item_id":3},{"item_id":4}]

@app.get("/")
async def index(skip:int = 0, limit:int=10):
    item = fake_items_db[skip: skip+limit]
    return item

# Example: http://127.0.0.1:8000/?skip=1&limit=2