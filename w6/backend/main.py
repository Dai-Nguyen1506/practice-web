from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

app = FastAPI()

app.mount("/static", StaticFiles(directory="../frontend"), name="static")

class HousePriceRequest(BaseModel):
    area: float = Field(..., gt=0, description="Area of the house in square meters")
    bedrooms: int = Field(..., ge=0, description="Number of bedrooms")
    location: str = "other"

class HousePricePrediction(BaseModel):
    area: float
    bedrooms: int
    location: str
    predicted_price: float

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/predict", response_model=HousePricePrediction)
def predict_price(data: HousePriceRequest):
    cost = 500000000 + data.area * 15000000 + data.bedrooms * 50000000

    if data.location == "hanoi":
        cost *= 1.2
    elif data.location == "hcmc":
        cost *= 1.5

    predict = HousePricePrediction(
        area=data.area,
        bedrooms=data.bedrooms,
        location=data.location,
        predicted_price=cost
    )

    return predict