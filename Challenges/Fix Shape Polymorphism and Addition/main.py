class Shape:
    def area(self):
        return 0

    def __add__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area() + other.area()


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width + self.height


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = 0


class CompositeShape(Shape):
    def __init__(self, shapes):
        self.shapes = list(shapes)

    def area(self):
        return len(self.shapes)
