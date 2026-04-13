from fastapi import FastAPI
from app.core.database import engine, Base, SessionLocal
from app.models import carApp


from sqlalchemy.orm import Session
from app.models.carApp import CarApp
from app.api.v1.endpoints.car import router as car_router

app = FastAPI()



from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://playful-tiramisu-85452d.netlify.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(car_router, prefix="/api/v1", tags=["Cars"])
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Backend running correctly"}

@app.get("/test-db")
def test_db():
    db:Session = SessionLocal()
    cars = db.query(CarApp).all()
    db.close()
    return {"total_cars":len(cars)}
    