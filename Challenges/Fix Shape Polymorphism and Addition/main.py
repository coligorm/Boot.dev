class Shape:
    def area(self):
        return 0

    def __add__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return CompositeShape([self, other])


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class CompositeShape(Shape):
    def __init__(self, shapes):
        self.shapes = list(shapes)

    def area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()
        return total
