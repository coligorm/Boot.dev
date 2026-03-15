class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def description(self):
        pass


class Drink(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def description(self):
        pass


class Dessert(MenuItem):
    def __init__(self, name, price, slices):
        super().__init__(name, price)
        self.slices = slices

    def description(self):
        pass
