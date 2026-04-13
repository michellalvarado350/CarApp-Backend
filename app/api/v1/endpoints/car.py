from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.carSchema import CarAppCreate, CarAppResponse, CarAppUpdate
from app.crud.car_crud import create_car, delete_car, update_car, get_all_cars
from app.models.carApp import CarApp

router = APIRouter()

# Dependencia para obtener sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/cars", response_model=CarAppResponse, status_code=201)
def create_new_car(car:CarAppCreate, db:Session = Depends(get_db)):
    return create_car(db, car)

@router.get("/cars", response_model=list[CarAppResponse])
def list_cars(
    skip:int = 0,
    limit:int= 10,
    marca:str | None=None,
    localidad:str | None=None,
    solicitante:str |None=None,
    sort_by:str | None=None,
    order:str = "desc",
    db: Session = Depends(get_db),
):
    return get_all_cars(
        db=db,
        skip=skip,
        limit=limit,
        marca=marca,
        localidad=localidad,
        solicitante=solicitante,
        sort_by=sort_by,
        order=order,
    )

@router.delete("/cars/{car_id}", response_model=CarAppResponse)
def remove_car(car_id:int, db:Session= Depends(get_db)):
    car = delete_car(db, car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Carro no encontrado")
    return car

@router.put("/cars/{car_id}", response_model = CarAppResponse)
def edit_car(car_id:int, car: CarAppUpdate, db:Session = Depends(get_db)):
    try:
        updated = update_car(db,car_id,car)
    except Exception:
        raise HTTPException(status_code=400, detail="Datos inválidos")
    if not updated:
        raise HTTPException(status_code=404, detail="Carro no encontrado")
    return updated
