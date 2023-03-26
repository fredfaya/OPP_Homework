from exercice1.accomodations.accomodation import Accomodation
from exercice1.cars.car import Car


class TravelAgency:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.accommodations = []
        self.cars = []

    def add_accommodations(self, accommodation: Accomodation):
        self.accommodations.append(accommodation)

    def add_vehicle(self, vehicle: Car):
        self.cars.append(vehicle)

    def check_in_accommodation(self, id: str, location: str):
        for accommodation in self.accommodations:
            if accommodation.id == id and accommodation.location == location:
                accommodation.set_availability(False)
                print(f"{accommodation.get_name()} at {location} is now occupied")
                return
        print("Accommodation not found")

    def check_out_accommodation(self, id, location):
        for accommodation in self.accommodations:
            if accommodation.id == id and accommodation.location == location:
                accommodation.set_availability(True)
                print(f"{accommodation.get_id()} at {location} is now available")
                return
        print("Accommodation not found")

    def rent_car(self, make: str, model: str, license_plate: str):
        for car in self.cars:
            if car.make == make and car.model == model and car.get_licence_plate_number() == license_plate:
                if car.get_is_rented():
                    print(f"This car Make: {car.make}, Model: {car.model}, Licence Plate Number: {car.licence_plate_number} is already rented.")
                else:
                    car.set_is_rented(True)
                    print(f"Car Make: {car.make}, Model: {car.model}, Licence Plate Number: {car.licence_plate_number} rented successfully.")
                return
        print(f"This car Make: {make}, Model: {model}, Licence Plate Number: {license_plate} is not available for rent.")

    def return_car(self, make: str, model: str, license_plate: str):
        for car in self.cars:
            if car.make == make and car.model == model and car.get_licence_plate_number() == license_plate:
                if car.get_is_rented():
                    car.set_is_rented(False)
                    print(f"Car Make: {car.make}, Model: {car.model}, Licence Plate Number: {car.licence_plate_number} returned successfully.")
                else:
                    print(f"This car Make: {car.make}, Model: {car.model}, Licence Plate Number: {car.licence_plate_number} is not currently rented.")
                return
        print(f"This car Make: {make}, Model: {model}, Licence Plate Number: {license_plate} is not in our rental fleet.")

    def rent_accommodation(self, id: str, location: str):
        for accommodation in self.accommodations:
            if accommodation.id == id and accommodation.location == location:
                if accommodation.get_availability():
                    print(f"This accommodation {accommodation. get_id()} located at {accommodation.get_location()} is already rented.")
                else:
                    accommodation.set_availability(True)
                    print(f"Accommodation {accommodation. get_id()} located at {accommodation.get_location()} rented successfully.")
                return
        print(f"This accommodation {id} located at {location} is not available for rent.")

    def return_accommodation(self, id: str, location: str):
        for accommodation in self.accommodations:
            if accommodation.id == id and accommodation.location == location:
                if accommodation.get_availability():
                    accommodation.set_availability(False)
                    print(f"Accommodation {accommodation. get_id()} located at {accommodation.get_location()} returned successfully.")
                else:
                    print(f"This accommodation {accommodation. get_id()} located at {accommodation.get_location()} is "
                          f"not currently rented.")
                return
        print(f"This accommodation {id} located at {location} is not in our rental fleet.")

    # to string method in order to print the object, accomm and cars are printed as well
    def __str__(self):
        accommodation_info = "\n".join([str(accommodation) for accommodation in self.accommodations])
        rental_car_info = "\n".join([str(rental_car) for rental_car in self.cars])
        return f"{self.name}\n{self.address}\n\nAccommodations:\n{accommodation_info}\n\nRental Cars:\n{rental_car_info}"
