# Challenge number 079: create a program that reads many values and put them in a ordered list. If the user insert a number that
#already exist, the program have to alert the user about it.
list = []
num = 0
while True:
    num = int(input('Say a number: '))
    if num not in list:
        list.append(num)
    else:
        print('This number is already in the list!!! Please, try again.')
    list.sort()
    ask = str(input('Do you want to continue? ')).strip().upper()
    if ask not in "YN":
        print('Invalide answer. Say Yes or No.')
        ask = str(input('Do you want to continue? ')).strip().upper()
        if ask == "N":
            break
print(list)





