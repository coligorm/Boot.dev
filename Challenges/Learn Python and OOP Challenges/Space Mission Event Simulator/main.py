class Ship:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 10
        self.cargo = {}

    def mine(self, item, amount, energy_cost):
        if self.energy - energy_cost < 0:
            return f"Skipped {item}"
        else:
            self.energy -= energy_cost
            if item not in self.cargo:
                self.cargo[item] = amount
            else:
                self.cargo[item] += amount
            return f"Mined {item} x{amount}"

    def take_hit(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0 
        return f"Took {damage} damage"

    def charge(self, amount):
        self.energy += amount
        return f"Charged {amount} energy"

    def repair(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
        return f"Repaired {amount} health"

    def is_destroyed(self):
        if self.health <= 0:
            return "Ship destroyed"

    def cargo_text(self):
        result = ""
        if len(self.cargo) == 0:
            result = "empty, "

        for i in self.cargo:
            result += f"{i}:{self.cargo[i]}, "

        return result[:-2]

        
class Mission:
    def __init__(self, ship, events):
        self.ship = ship
        self.events = events
        self.log = []

    def run(self):
        for event in self.events:
            match event["type"]:
                case "mine":
                    self.log.append(self.ship.mine(event["item"], event["amount"], event["energy"]))
                case "hit":
                    self.log.append(self.ship.take_hit(event["damage"]))
                    if self.ship.is_destroyed() == "Ship destroyed":
                        self.log.append(self.ship.is_destroyed())
                        break
                case "charge":
                    self.log.append(self.ship.charge(event["energy"]))
                case "repair":
                    self.log.append(self.ship.repair(event["health"]))

def simulate_mission(name, events):
    summary = {}
    ship = Ship(name)
    mission = Mission(ship, events)
    mission.run()
    
    summary["pilot"] = name
    summary["health"] = ship.health
    summary["energy"] = ship.energy
    summary["cargo"] = ship.cargo
    summary["cargo_text"] = ship.cargo_text()
    summary["log"] = mission.log

    return summary
