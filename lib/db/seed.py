from random import choice as rc
from database import Session
from db.models import Car, Service


cars_data = [
    {'make': 'Toyota', 'model': 'Camry'},
    {'make': 'Honda', 'model': 'CRV'},
    {'make': 'Nissan', 'model': 'Rouge'},
    {'make': 'Mazda', 'model': 'CX5'},
    {'make': 'Kia', 'model': 'k5'}
]

services_data = [
    {'date': '2023-08-15', 'description': 'Oil Change', 'cost': 50},
    {'date': '2023-07-20', 'description': 'Brake Inspection', 'cost': 30},
    {'date': '2023-06-10', 'description': 'Oil Change', 'cost': 60},
    {'date': '2023-05-02', 'description': 'Brake replace', 'cost': 100},
    {'date': '2023-03-15', 'description': 'Tires Change', 'cost': 150},
    {'date': '2023-01-25', 'description': 'Brake Inspection', 'cost': 130}
]


def create_cars():
    for car_data in cars_data:
        car = Car(
            make=car_data['make'],
            model=car_data['model']
        )
        Session.add(car)
        Session.commit()

def create_services():
    for service_data in services_data:
        service = Service(
            date=service_data['date'],
            description=service_data['description'],
            cost=service_data['cost']
        )
        Session.add(service)
        Session.commit()

def create_cars_services():
    cars = Session.query(Car).all()
    services = Session.query(Service).all()
    for car in cars:
        for service in services:
            car.services.append(service)
    Session.commit()

def remove_cars_services(car_id, service_id):
    car = Session.query(Car).filter_by(id=car_id).first()
    service = Session.query(Service).filter_by(id=service_id).first()

    if car and service:
        car.services.remove(service)
        Session.commit()
    else:
        print('Car or Service not found.')
        
def main():
    create_cars()
    create_services()
    create_cars_services()
    # remove_cars_services(car_id=9, service_id=10)
    Session.close()


if __name__ == '__main__':
   main()


