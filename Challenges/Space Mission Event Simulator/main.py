class Ship:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 10
        self.cargo = {}

    def mine(self, item, amount, energy_cost):
        pass

    def take_hit(self, damage):
        pass

    def charge(self, amount):
        pass

    def repair(self, amount):
        pass

    def is_destroyed(self):
        pass

    def cargo_text(self):
        pass


class Mission:
    def __init__(self, ship, events):
        self.ship = ship
        self.events = events
        self.log = []

    def run(self):
        pass


def simulate_mission(name, events):
    pass
