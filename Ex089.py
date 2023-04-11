# Chllenge number 089: create a program that reads the name and two grades of many students.
# After that, show a table with the average grade of each one, and allow the user to see details about each student.
# I am allowed to use only lists!!!!
list1 = list()
list2 = list()
while True:
    name = str(input('Name: '))
    grade1 = float(input('Grade-1: '))
    grade2 = float(input('Grade-2: '))
    average = (grade1+grade2)/2
    ask = str(input('Do you want to continue? ')).strip().upper()
    list1.append([name, [grade1, grade2], average])
    if ask not in 'YN':
        print('Invalid answer. Please enter Y or N.')
        ask = str(input('Do you want to continue? ')).strip().upper()
    if ask in 'N':
        break
print('-='*30)
print(list1)
print('-='*30)
print(f'{"Nº":<4}{"Name":<10}{"Average":>8}')
for i, s in enumerate(list1):
    print(f'{i:<4}{s[0]:<10}{s[2]:>8}')
while True:
    print('~-'*30)
    detail = int(input('Which student do you want to see in detail? enter 999 to stop '))
    if detail == 999:
        print('<<< Good Bye! >>>')
        break
    if detail <= len(list1) - 1:
       print(f'The grades of {list1[detail][0]} are: {list1[detail][1]}')









