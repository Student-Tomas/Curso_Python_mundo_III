# Challenge number 082: receive numbers from the user and put them in a list. After that, divide this list in two others.
# one with even numbers and the other with odd numbers.
list = []
even_list = []
odd_list = []
while True:
    num = (int(input('Say a number: ')))
    list.append(num)
    ask = str(input('Do you want to continue? (Y or N) ')).strip().upper()
    if ask not in 'YN':
        print('Invalid answer!!!! Plese enter only Y or N')
        ask = str(input('Do you want to continue? (Y or N) ')).strip().upper()
    if ask == 'N':
        break
print('~='*30)
list.sort()
print(f'The whole list is: {list}')
for i in list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(f'The even list is: {even_list}')
print(f'The odd list is: {odd_list}')

