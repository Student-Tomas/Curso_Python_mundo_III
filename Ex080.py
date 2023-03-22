# Challenge number 080: create a program that receive five numbers from the user and put them in a ordered list, without using "sort()"
list = list()
for i in range(0, 5):
    num = int(input('Say a number: '))
    if i == 0:
        list.append(num)
        print('Number inserted in the first position')
    elif num > list[-1]:
        list.append(num)
        print('Number inserted in the last position')
    else:
        pos = 0
        while pos < len(list):
            if num <= list[pos]:
                list.insert(pos, num)
                print(f'Number inserted in the {pos} position')
                break
            pos += 1
print(list)


