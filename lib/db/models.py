from sqlalchemy import create_engine, Column, Table, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from helpers import (get_database_url)


# DATABASE_URL = get_database_url()
# engine = create_engine(DATABASE_URL)
Base = declarative_base()

car_service = Table(
    'car_service',
    Base.metadata,
    Column('car_id', Integer, ForeignKey('cars.id'), primary_key=True),
    Column('service_id', Integer, ForeignKey('services.id'), primary_key=True)
)

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)

    services = relationship("Service", secondary=car_service, back_populates="cars")

    def __repr__(self):
        return f'make: {self.make}\n, model: {self.model})'

class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    description = Column(String)
    cost = Column(Integer)

    cars = relationship('Car', secondary=car_service, back_populates='services')

    def __repr__(self):
        return f'date: {self.date}\n, description: {self.description}\n, cost: {self.cost}\n)'



