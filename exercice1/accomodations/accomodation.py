class Accomodation:
    def __init__(self, id: str, location: str, price_per_night: float):
        self.id = id
        self.location = location
        self.price_per_night = price_per_night
        self.availability = False

    def get_id(self) -> str:
        return self.id

    def set_id(self, id: str):
        self.id = id

    def get_location(self) -> str:
        return self.location

    def set_location(self, location: str):
        self.location = location

    def get_price_per_night(self) -> float:
        return self.price_per_night

    def set_price_per_night(self, price_per_night: float):
        self.price_per_night = price_per_night

    def get_availability(self) -> bool:
        return self.availability

    def set_availability(self, availability: bool):
        self.availability = availability

    def check_in(self):
        self.set_availability(False)
        print(f"Check in opereation : {self. get_id()} located at {self.get_location()} now occupied")

    def check_out(self):
        self.set_availability(True)
        print(f"Check out opereation : {self. get_id()} located at {self.get_location()} now available")

    def __str__(self):
        return f"Accomodation {self. get_id()} located at {self.get_location()} available for rent for {self.price_per_night} per night."