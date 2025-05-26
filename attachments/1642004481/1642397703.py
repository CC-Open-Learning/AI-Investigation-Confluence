import sys

Digits = [
    [' *** ', ' * * ', '*   *', '*   *', '*   *', ' * * ', ' *** '], # Zero
    ['  *  ', ' **  ', '  *  ', '  *  ', '  *  ', '  *  ', ' *** '], # One
    # Additional digits here
]

def print_big_digits(digits):
    for row in range(7):
        line = ''
        for digit in digits:
            number = int(digit)
            line += Digits[number][row] + '  '
        print(line)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print_big_digits(sys.argv[1])
    else:
        print("Usage: python bigdigits.py <number>")
