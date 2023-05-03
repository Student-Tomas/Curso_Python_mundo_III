# Challenge 094: Get the name, age and sex of a group of people. Put this information in a dictionary. After that, use
# a list to extract some data: average age, how many female, total of people, which one is above age average.
group = list()
person = dict()
age_sum = average_age = 0
while True:
    person.clear()
    person['name'] = str(input('Name: '))
    while True:
        person['gender'] = str(input('Gender (enter M or F):  ')).strip().upper()[0]
        if person['gender'] in "MF":
            break
        print('Error! Please enter only M or F.')
    person['age'] = int(input('Age: '))
    age_sum += person['age']
    group.append(person.copy())
    while True:
        ask = str(input('Do you want to continue (Y or N)? ')).strip().upper()[0]
        if ask in "YN":
            break
        print('Error! Enter only Y or N:')
    if ask == "N":
        break
print('-='*30)
print(group)
print('-='*30)
print(f'There are {len(group)} people registered.')
average_age = age_sum / len(group)
print(f"The age's averade is {average_age}")
print('The women registered are: ', end='')
for p in group:
    if p['gender'] in 'F':
        print(f'{p["name"]} ', end='')
print(f"\nList of people above age's average: ", end='')
for p in group:
    if p['age'] >= average_age:
        print(f"{p['name']}", end='')







