def print_table(height, length=3, symbol='++++'):
    for y in range(height):
        for x in range(length):
            print(f'|{symbol}', end='')
        print('|\n')


print_table(5, length=5, symbol='____')
