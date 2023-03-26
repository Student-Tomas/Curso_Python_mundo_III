# Challenge number 086: from a list of nine numbers, create a formated matrix.
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for row in range(0, 3):
    for column in range(0, 3):
        matrix[row][column] = int(input(f'Type a value for [{row}, {column}]: '))
print(f'{matrix}')
for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[row][column]:^5}]', end=' ')
    print()
