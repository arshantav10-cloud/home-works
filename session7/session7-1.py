# define a class(blueprint)
class Rectangle:
    # magic method
    def __init__(self, w, h) -> None:
        # use init to initialize attributes
        # attributes: width, height
        self.width = w
        self.height = h

    # 2 methods
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# objects
r1 = Rectangle(4, 10)
r2 = Rectangle(6, 9)

# print(r1.width, r1.height)
print(r1.area())
print(r1.perimeter())
