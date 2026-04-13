from pydantic import BaseModel, Field
from datetime import datetime

class CarAppBase(BaseModel):
    marca: str = Field(..., min_length=2, max_length=100)
    localidad:str = Field(..., min_length=3, max_length=100)
    solicitante:str = Field(..., min_length=3, max_length=100)
    
class CarAppCreate(CarAppBase):
    pass

class CarAppUpdate(CarAppBase):
    pass

class CarAppResponse(CarAppBase):
    id:int
    creado:datetime
    
    class Config:
        from_attributes = True
        
class CarAppUpdate(BaseModel):
    marca:str
    localidad:str
    solicitante:str
    