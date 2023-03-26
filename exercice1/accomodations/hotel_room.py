from exercice1.accomodations.accomodation import Accomodation


class HotelRoom(Accomodation):
    def __init__(self, id: str, location: str, price_per_night: float, type: str):
        super().__init__(id, location, price_per_night)
        self.type = type

    def get_type(self) -> str:
        return self.type

    def set_type(self, type:str):
        self.type = type
