class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def __str__(self):
        return f"{self.name}: Animal"

    def __eq__(self, other):
        return self.name == other.name


class Dog(Animal):
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
        return Pack([self.animals, other.animals])

    def sounds(self):
        lines = []
        for animal in self.animals:
            lines.append(f"{animal} says {Animal.speak(animal)}")
        return lines
