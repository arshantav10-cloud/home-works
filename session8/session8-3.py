class Polygon:
    """
    The class Polygon represents a regular polygon.
    """

    def __init__(self, number_of_sides) -> None:
        # initialize attributes(n)
        self.n = number_of_sides

    def get_sum_of_interior_angles(self):
        return (self.n - 2) * 180

    def get_each_interior_angle(self):
        return (self.n - 2) * 180 // self.n

    def get_each_exterior_angle(self):
        return 360 // self.n

    def get_number_of_diagonals(self):
        return (self.n * (self.n - 3)) // 2


for i in range(3, 11):
    shape = Polygon(i)
    print(f'sum of interior angles({i}-sided): {shape.get_sum_of_interior_angles()}')
    print(f'each interior angles({i}-sided): {shape.get_each_interior_angle()}')
    print(f'each exterior angles({i}-sided): {shape.get_each_exterior_angle()}')
    print(f'number of diagonals angles({i}-sided): {shape.get_number_of_diagonals()}')
    print('------------------------------------------------')
