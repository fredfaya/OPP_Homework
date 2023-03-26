class Wagon:
    def __init__(self, position, maximum_load):
        self.position = position
        self.maximum_load = maximum_load
        self.current_load = 0
        self.commodities = []
        self.full = False

    def get_current_load(self):
        return self.current_load

    def set_current_load(self, current_load):
        self.current_load += current_load

    def set_full(self, full):
        self.full = full

    def get_commodities(self):
        return self.commodities

    def add_commodity(self, commodity):
        self.commodities.append(commodity)