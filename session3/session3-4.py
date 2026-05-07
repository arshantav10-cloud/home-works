def find_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c


num1 = float(input('enter number1 number: '))
num2 = float(input('enter number2 number: '))
num3 = float(input('enter number3 number: '))

print(find_max(num1, num2, num3))
