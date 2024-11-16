from fastapi import FastAPI
from server.services.price import get_price

app = FastAPI()


@app.get("/price")
def read_price():
    get_price()
    return {"price": 100}


@app.get("/pool")
def read_pool():
    return {"price": 100}
