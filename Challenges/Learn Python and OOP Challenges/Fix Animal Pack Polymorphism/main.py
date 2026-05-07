class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __eq__(self, other):
        return self.name == other.name and self.__class__.__name__ == other.__class__.__name__


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "meow"


class Parrot(Animal):
    def speak(self):
        return "squawk"


class Pack:
    def __init__(self, animals):
        self.animals = animals

    def __add__(self, other):
        new_pack = []
        for animal in self.animals:
            new_pack.append(animal)
        for animal in other.animals:
            new_pack.append(animal)
        return Pack(new_pack)

    def sounds(self):
        lines = []
        for animal in self.animals:
            lines.append(f"{animal} says {animal.speak()}")
        return lines
