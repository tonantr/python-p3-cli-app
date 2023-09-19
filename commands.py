from models import Car, Service, car_service
from helpers import is_valid_date, is_valid_cost, is_valid_id
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


def get_user_input_carid():
    while True:
        car_id = input("Enter car ID: ")
        if not is_valid_id(car_id):
            print("Invalid car ID format")
        else:
            car = session.query(Car).get(int(car_id))
            if not car:
                print("Car not found")
            else:
                break
    return int(car_id)


def get_user_input_serviceid():
    while True:
        service_id = input("Enter service ID: ")
        if not is_valid_id(service_id):
            print("Invalid service ID format")
        else:
            service = session.query(Service).get(service_id)
            if not service:
                print("Service not found")
            else:
                break
    return int(service_id)


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


def add_car_service():
    car_id = get_user_input_carid()
    service_id = get_user_input_serviceid()
    association = car_service.insert().values(car_id=car_id, service_id=service_id)
    session.execute(association)
    session.commit()
    return


def view_cars():
    cars = session.query(Car).all()
    if not cars:
        print("No cars found in the database")
    else:
        print("List of Cars:")
        for car in cars:
            print(f"\nID: {car.id}, Make: {car.make}, Model: {car.model}")


def view_services():
    services = session.query(Service).all()
    if not services:
        print("No services found in the database")
    else:
        print("List of Services:")
        for service in services:
            print(
                f"\nID: {service.id}, Date: {service.date}, Description: {service.description}, Cost: {service.cost}"
            )


def get_services_for_car():
    car_id = get_user_input_carid()
    car = session.query(Car).get(car_id)
    if car:
        for service in car.services:
            print(
                f"\nService ID: {service.id}, Date: {service.date}, Description: {service.description}, Cost: {service.cost}"
            )
    else:
        print("No Services found for this car.")


def get_cars_for_service():
    service_id = get_user_input_serviceid()
    service = session.query(Service).get(service_id)
    if service:
        for car in service.cars:
            print(f"\nCar ID: {car.id}, Make: {car.make}, Model: {car.model}")
    else:
        print("No Cars found for this service.")
