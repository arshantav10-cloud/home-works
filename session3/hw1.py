from random import choice, shuffle
from string import ascii_lowercase, ascii_uppercase, digits


def random_pass(length=8):
    """ This function generates a random string """
    password_list = [choice(ascii_lowercase), choice(ascii_uppercase), choice(digits)]
    for i in range(length - 3):
        password_list.append(choice(ascii_lowercase + ascii_uppercase + digits))

    shuffle(password_list)

    return ''.join(password_list)


print(random_pass(12))
print(random_pass(10))
print(random_pass(6))
print(random_pass(20))
print(random_pass())
