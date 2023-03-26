class Commodity:
    def __init__(self, designation, weight, owner):
        self.designation = designation
        self.weight = weight/1000
        self.owner = owner

    def __str__(self):
        return f"{self.designation} ({self.weight} kg), owned by {self.owner}"