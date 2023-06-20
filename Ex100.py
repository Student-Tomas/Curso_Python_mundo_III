# Challenge number 100: create two functions, one to create a random list with five numbers, and other to sum
# only the evem numbers of this list.

from random import randint
from time import sleep

def numbers(group):
    print(f'The list of random numbers is: ', end="")
    for cont in range(0, 5):
        n = randint(0, 10)
        group.append(n)
        sleep(0.3)
        print(f'{n} ', end="")


def evem_sum(group):
    sum = 0
    for n in group:
        if n % 2 == 0:
            sum += n
    print(f'\nAnd the sum of its evem numbers is: {sum}.')


# Main program
group = list()
numbers(group)
evem_sum(group)

