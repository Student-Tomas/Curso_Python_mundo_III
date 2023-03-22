#Challenge number 074: choose five numbers randomly and put them in a tuple. After that,
# show the chosen numbers and say which one is the biggest and the smallest
from random import randint
num = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'The numbers chosen are: {num}')
# or I can use for to show the list
#for i in num:
 #   print(f'{i} ', end='')
print(f'The biggest number is {max(num)}')
print(f'The smallest number is {min(num)}')


