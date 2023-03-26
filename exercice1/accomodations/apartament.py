from exercice1.accomodations.accomodation import Accomodation


class Apartament(Accomodation):
    def __init__(self, id: str, location: str, price_per_night: float, number_of_rooms: int):
        super().__init__(id, location, price_per_night)
        self.number_of_rooms = number_of_rooms

    def get_number_of_rooms(self) -> int:
        return self.number_of_rooms

    def set_number_of_rooms(self, number_of_rooms: int):
        self.number_of_rooms = number_of_rooms


