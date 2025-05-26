import random

def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print('must be >=', minimum)
            else:
                return i
        except ValueError as err:
            print(err)

rows = get_int('rows: ', 1, None)
columns = get_int('columns: ', 1, None)
minimum = get_int('minimum (or Enter for 0): ', -1000000, 0)
maximum = get_int('maximum (or Enter for 1000): ', minimum, 1000)

row = 0
while row < rows:
    line = ''
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)
        s = str(i)
        line += s
        column += 1
        if column < columns:
            line += ', '
    print(line)
    row += 1
