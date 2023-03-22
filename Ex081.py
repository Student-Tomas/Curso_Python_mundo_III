# Challenge 080: get a list of numbers from the user. Say how many itens there are in the list and if the number
# five is in this list.
list = []
while True:
    num = int(input('Say a number: '))
    list.append(num)
    print(list)
    ask = str(input('Do you want to continue? (Y or N)? ')).strip().upper()
    if ask not in "YN":
        print('Invalid answer. Please enter Y or N.')
        ask = str(input('Do you want to continue? (Y or N)? ')).strip().upper()
    if ask == "N":
        break
print('~='*30)
new_list = sorted(list, reverse=True)
print(f'The list in reverse order is: {new_list}')
print('~='*30)
if 5 in list:
    print("The number five is in the list")
else:
    print('There is no number five in the list.')
# The oder way is below
'''list = list()
while True:
    list.append(int(input('Say a number: ')))
    ask = str(input('Do you want to continue? [Y or N] ')).strip().upper()
    while ask not in 'YN':
        print('Invalid answer!Please enter Y or N.')
        ask = str(input('Do you want to continue? [Y or N] ')).strip().upper()
    if ask == 'N':
        break
print('~='*30)
list.sort(reverse=True)
print(f'The list in descending order is: {list}')
print('~='*30)
if 5 in list:
    print("The number five is in the list")
else:
    print('There is no number five in the list.')
print('~='*30)'''

