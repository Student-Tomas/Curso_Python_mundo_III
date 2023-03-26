# Challenge number 085: creat a list with sevem numbers and separate these number two lists, one with odd and the other
# with evem numbers.
list = [[], []]
for i in range(1, 8):
    num = int(input(f'Number {i}: '))
    if num % 2 == 0:
        list[0].append(num)
    else:
        list[1].append(num)
print('~='*30)
list[0].sort()
list[1].sort()
print(f'The odd list is: {list[0]}')
print(f'The evem list is: {list[1]}')




