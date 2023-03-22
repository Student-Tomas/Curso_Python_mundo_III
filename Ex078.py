# Challente number 078: create a program that reads five numbers and put them in a list. After that, sy which one is the greatest and the smallest with irs own position
values = []
for value in range(0, 5):
    values.append(int(input('Say a number: ')))
print(values)
print(f'The greatest value is {max(values)} and it is in position', end=" ")
great = max(values)
for i, v in enumerate(values):
    if v == great:
        print(f'{i+1} ...',end=" ")
print(f'\nThe smallest value is {min(values)} and it is in position', end=" ")
small = min(values)
for i, v in enumerate(values):
    if v == small:
        print(f'{i+1} ...', end=" ")



