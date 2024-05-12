from enum import Enum
from .base import Base
from sqlalchemy import Column, Integer, String, Float, Enum as Enum_SQLALCHEMY


class FuelChoices(Enum):
    Gasoline = 'Gasoline'
    Diesel = 'Diesel'
    Gas = 'Gas'


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    model_name = Column(String(50), primary_key=True)
    engine = Column(Float, primary_key=True)
    type_of_fuel = Column(Enum_SQLALCHEMY(FuelChoices, name="fuelchoices_type", create_type=True), nullable=False)

