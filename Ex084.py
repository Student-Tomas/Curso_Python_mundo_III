# Challenge number 084: create a program that receives some names of people and their weights. After that, say how many people
# was entered, who is the heaviest and the lightest.
list = []
data = []
while True:
    name = str(input('Name: ')).strip()
    weight = float(input('weight: '))
    data.append(list[:])
    ask = str(input('Do you want to continue? Y or N ')).strip().upper()
    if ask == 'N':
        break
print(list)
print(data)
