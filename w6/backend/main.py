from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="../frontend"), name="static")

class HouseInput(BaseModel):
    area: float
    bedrooms: int
    location: str = "other"

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/predict")
def predict_price(area: float, bedrooms: int, location: str = "other") -> float:
    cost = 500000000 + area * 15000000 + bedrooms * 50000000

    if location == "hanoi":
        cost *= 1.2
    elif location == "hcmc":
        cost *= 1.5

    return {
        "area": area,
        "bedrooms": bedrooms,
        "location": location,
        "predicted_price": cost
    }

@app.post("/predict")
def predict_price_post(house: HouseInput):
    cost = 500000000 + house.area * 15000000 + house.bedrooms * 50000000

    if house.location == "hanoi":
        cost *= 1.2
    elif house.location == "hcmc":
        cost *= 1.5

    return {
        "area": house.area,
        "bedrooms": house.bedrooms,
        "location": house.location,
        "predicted_price": cost
    }