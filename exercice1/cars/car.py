class Car:
    def __init__(self, make: str, model: str, licence_plate_number: str, price: int):
        self.make = make
        self.model = model
        self.licence_plate_number = licence_plate_number
        self.price = price
        # variable created to know if the car is rented or not
        self.is_rented = False

    # getter of make
    def get_make(self) -> str:
        return self.make

    # setter of make
    def set_make(self, make: str):
        self.make = make

    # getter of model
    def get_model(self) -> str:
        return self.model

    # setter of model
    def set_model(self, model: str):
        self.model = model

    # getter of licence plate number
    def get_licence_plate_number(self) -> str:
        return self.licence_plate_number

    # setter of licence plate number
    def set_licence_plate_number(self, licence_plate_number: str):
        self.licence_plate_number = licence_plate_number

    # getter of price
    def get_price(self) -> int:
        return self.price

    # setter of price
    def set_price(self, price: int):
        self.price = price

    def get_is_rented(self) -> bool:
        return self.is_rented

    def set_is_rented(self, is_rented: bool):
        self.is_rented = is_rented

    # pickup function
    def pickup(self):
        print("Car is ready to be picked up")

    # deliver function
    def deliver(self):
        print("Car is ready to be delivered")

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Licence Plate Number: {self.licence_plate_number}, Price: {self.price}, Is Rented: {self.is_rented}"
