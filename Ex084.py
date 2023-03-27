# Challenge number 084: create a program that receives some names of people and their weights. After that, say how many people
# was entered, who is the heaviest and the lightest.
list = []
data = []
greatest = lowest = 0
while True:
    name = str(input('Name: ')).strip()
    weight = float(input('weight: '))
    list.append(name)
    list.append(weight)
    if len(data) == 0:
        greatest = lowest = list[1]
    else:
        if list[1] > greatest:
            greatest = list[1]
        if list[1] < lowest:
            lowest = list[1]
    data.append(list[:])
    list.clear()
    ask = str(input('Do you want to continue? Y or N ')).strip().upper()
    if ask == 'N':
        break
print('~='*30)
print(data)
print(f'The user inserted {len(data)} people in the list.')
print(f'The greatest weight is {greatest}:', end=' ')
for p in data:
    if p[1] == greatest:
        print(f'[{p[0]}]', end=' ')
print(f'\nThe lowest weight is {lowest}:', end=' ')
for p in data:
    if p[1] == lowest:
        print(f'[{p[0]}]', end=' ')


