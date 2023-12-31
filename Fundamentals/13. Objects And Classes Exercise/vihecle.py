class Vehicle:

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, new_owner):
        if money < self.price:
            return "Sorry, not enough money"
        if self.owner is not None:
            return "Car already sold"

        self.owner = new_owner
        return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"

        return f"{self.model} {self.type} is on sale: {self.price}"