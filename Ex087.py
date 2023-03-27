# Challenge number 087: make a formated matrix with nine numbers and show the sum of the evem numbers,
# the greatest value of the second row, and the sum of the thyrd column.
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
evem_sum = sum_3_column = great_2_row = 0
for row in range(0, 3):
    for column in range(0, 3):
        num = int(input(f'Enter a number for the position [{row, column}]: '))
        matrix[row][column] = num
        if num % 2 == 0:
            evem_sum += num
print(matrix)
for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[row][column]:^5}]', end=' ')
    print()
print(f'The sum of all evem numbers is: {evem_sum}.')
for row in range(0, 3):
    sum_3_column += matrix[row][2]
print(f'The sum of the 3rd column numbers is {sum_3_column}')
for column in range(0, 3):
    if column == 0:
        great_2_row = matrix[1][column]
    elif matrix[1][column] > great_2_row:
        great_2_row = matrix[1][column]
print(f'The greatest value of the second row is {great_2_row}.')


