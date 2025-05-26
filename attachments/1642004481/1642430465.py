import cmath
import sys

def get_float(msg, allow_zero):
    while True:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print('zero is not allowed')
                continue
            return x
        except ValueError as err:
            print(err)

print('ax² + bx + c = 0')
a = get_float('enter a: ', False)
b = get_float('enter b: ', True)
c = get_float('enter c: ', True)

x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)

if discriminant == 0:
    x1 = -b / (2 * a)
    print(f'There is a double root at {x1}')
else:
    sqrt_discriminant = cmath.sqrt(discriminant)
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    print(f'The roots are {x1} and {x2}')
