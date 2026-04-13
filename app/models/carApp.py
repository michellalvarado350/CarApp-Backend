from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base

class CarApp(Base):
    __tablename__ = "car_apps"
    
    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    localidad = Column(String, nullable=False)
    solicitante = Column(String,nullable=False)
    creado = Column(DateTime, default=datetime.utcnow)
    