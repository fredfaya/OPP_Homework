class Warehouse:
    def __init__(self, location):
        self.location = location
        self.inventory = []

    def receive(self, commodity):
        self.inventory.append(commodity)

    def get_commodities(self):
        return self.inventory

    def delete_commodity(self, commodity):
        self.inventory.remove(commodity)

    def __str__(self):
        inventory_str = "\n".join([str(commodity) for commodity in self.inventory])
        return f"Warehouse in {self.location}:\nTo ship:[{inventory_str}]"
