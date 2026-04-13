from sqlalchemy.orm import Session
from app.models.carApp import CarApp
from app.schemas.carSchema import CarAppCreate, CarAppUpdate

def create_car(db:Session, car:CarAppCreate):
    db_car = CarApp(
        marca = car.marca,
        localidad = car.localidad,
        solicitante = car.solicitante
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    
    return db_car

def get_all_cars(
    db:Session,
    skip:int=0,
    limit:int=10,
    marca:str | None=None,
    localidad:str | None=None,
    solicitante:str | None=None,
    sort_by:str | None=None,
    order:str = "desc",
):
    query = db.query(CarApp)
    
    if marca:
        print("Filtrando por marca:",marca)
        query = query.filter(CarApp.marca.ilike(f"%{marca}%"))
        
    if localidad:
        query = query.filter(CarApp.localidad.ilike(f"%{localidad}%"))
        
    if solicitante:
        query = query.filter(CarApp.solicitante.ilike(f"%{solicitante}%"))
        
    if sort_by:
        column = getattr(CarApp, sort_by, None)
    else:
        column = CarApp.id
        
    if column is not None:
        if order == "desc":
            query = query.order_by(column.desc())
        else:
            query = query.order_by(column.asc())
        
    return query.offset(skip).limit(limit).all()
    
def delete_car(db:Session, car_id:int):
    car = db.query(CarApp).filter(CarApp.id == car_id).first()
    
    if not car:
        return None
    db.delete(car)
    db.commit()
    
    return car

def update_car(db:Session, car_id:int, car_data: CarAppUpdate):
    car = db.query(CarApp).filter(CarApp.id == car_id).first()
    
    if not car:
        return None
    
    car.marca = car_data.marca
    car.localidad = car_data.localidad
    car.solicitante = car_data.solicitante
    
    db.commit()
    db.refresh(car)
    
    return car