class Ability:
    def __init__(self, name):
        self.name = name

    def power(self):
        pass

    def __add__(self, other):
        pass

    def __gt__(self, other):
        pass


class FireAbility(Ability):
    def __init__(self, name, flames):
        super().__init__(name)
        self.flames = flames

    def power(self):
        pass


class IceAbility(Ability):
    def __init__(self, name, shards):
        super().__init__(name)
        self.shards = shards

    def power(self):
        pass


class WindAbility(Ability):
    def __init__(self, name, gusts):
        super().__init__(name)
        self.gusts = gusts

    def power(self):
        pass


def get_strongest_ability(abilities):
    pass
