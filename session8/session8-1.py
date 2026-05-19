from math import pi


class Circle:
    def __init__(self, r) -> None:
        self.radius = r

    def area(self):
        return round(self.radius ** 2 * pi, 2)

    def perimeter(self):
        return round(2 * self.radius * pi, 2)


c1 = Circle(5)
print(c1.area())
print(c1.perimeter())

c2 = Circle(1.1)
print(c2.area())
print(c2.perimeter())
