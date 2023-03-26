from exercice1.cars.car import Car


class Electric(Car):
    def __init__(self, make, model, licence_plate_number, price):
        super().__init__(make, model, licence_plate_number, price)