# Challenge 094: Get the name, age and sex of a group of people. Put this information in a dictionary. After that, use
# a list to extrate some data: average age, how many female, total of people, which one is above age average.
group = list()
person = dict()
while True:
    person['name'] = str(input('Name: '))
    while True:
        person['gender'] = str(input('Gender (enter M or F):  ')).strip().upper()[0]
        if person['gender'] in "MF":
            break
        print('Error! Please enter only M or F.')
    person['age'] = int(input('Age: '))
    while True:
        ask = str(input('Do you want to continue (Y or N)? ')).strip().upper()[0]
        if ask in "YN":
            break
        print('Error! Enter only Y or N:')
    if ask == "N":
        break

print(person)

