from math import pi
from cobra_color import cstr


def get_rectangle_area(width: float | int, length: float | int) -> float | int:
    """ Return the area of a rectangle with given width and length. """
    return width * length


def get_circle_area(radius: float | int) -> float | int:
    """return the area of a circle with given radius."""
    return radius ** 2 * pi


def is_it_even(num: int | float) -> bool:
    """Return True if num is even, otherwise return False."""
    return num % 2 == 0


def analyse_polygon(num: int) -> None:
    """Analyse a polygon with given length."""
    print("---------------------------------------------")
    print(cstr(f'The sum of interior angels of {num}-sided regular polygon: {(num - 2) * 180}', fg=(220, 40, 20),
               styles=["bold"]))
    print(cstr(f'each interior angel of {num}-sided regular polygon: {((num - 2) * 180) // num}', fg=(0, 255, 0)))
    print(
        cstr(f'each exterior angel of {num}-sided regular polygon: {360 // num}', fg=(255, 255, 0), styles=["italic"]))
    print(cstr(f'number of diagonal of {num}-sided regular polygon: {(num * (num - 3)) // 2}', fg=(0, 255, 255)))


def is_prime(num: int) -> bool:
    """Return True if num is prime, otherwise return False."""
    pass


def fact(num: int) -> int:
    """Return the factorial of num."""
    # n! = 1 * 2 * 3 *  ... * n
    # 5! = 1 * 2 * 3 * 4 * 5 --> 120
    pass


def average(nums: list) -> float:
    """Return the average of nums."""
    pass


def fun():
    return cstr("Hello World!", fg=(255, 255, 0), styles=["bold"])
