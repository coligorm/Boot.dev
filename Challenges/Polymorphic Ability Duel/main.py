class Ability:
    def __init__(self, name):
        self.name = name

    def power(self):
        return 0

    def __add__(self, other):
        return self.power() + other.power()

    def __gt__(self, other):
        return self.power() > other.power()


class FireAbility(Ability):
    def __init__(self, name, flames):
        super().__init__(name)
        self.flames = flames

    def power(self):
        return self.flames * 4


class IceAbility(Ability):
    def __init__(self, name, shards):
        super().__init__(name)
        self.shards = shards

    def power(self):
        return self.shards * 3


class WindAbility(Ability):
    def __init__(self, name, gusts):
        super().__init__(name)
        self.gusts = gusts

    def power(self):
        return self.gusts + 5


def get_strongest_ability(abilities):
    if len(abilities) == 0:
        return None

    strongest = abilities[0]
    
    for abilitie in abilities:
        if abilitie > strongest:
            strongest = abilitie
    return strongest.name
