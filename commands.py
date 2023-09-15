from models import Car, Service
from helpers import is_valid_date, is_valid_cost
from database import session



def get_user_input_car():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    return make, model


def get_user_input_service():
    while True:
        date = input("Enter service date (YYYY-MM-DD): ")
        if not is_valid_date(date):
            print("Invalid date format")
        else:
            break

    description = input("Enter service description: ")
    
    while True:
        cost = input("Enter service cost: ")
        if not is_valid_cost(cost):
            print("Invalid cost format")
        else:
            int(cost)
            break

    return date, description, cost


def add_car():
    make, model = get_user_input_car()
    car = Car(make=make, model=model)
    session.add(car)
    session.commit()
    return


def add_service():
    date, description, cost = get_user_input_service()
    service = Service(date=date, description=description, cost=cost)
    session.add(service)
    session.commit()
    return

def view_cars():
    cars = session.query(Car).all()
    if not cars:
        print('No cars found in the database')
    else:
        print('List of Cars:')
        for car in cars:
            print(f'ID: {car.id}, Make: {car.make}, Model: {car.model}')

def view_services():
    services = session.query(Service).all()
    if not services:
        print('No services found in the database')
    else:
        print('List of Services:')
        for service in services:
            print(f'ID: {service.id}, Date: {service.date}, Description: {service.description}, Cost: {service.cost}')

