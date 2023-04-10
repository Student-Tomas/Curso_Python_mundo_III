# Challenge number 088: create a program that gives sugestions to bet in the lotery.
# six different random numbers from zero to sixty, how many times the user want.
'''import random, time
num = int(input('How many times do you want to bet? '))
for i in range(0, num):
    print(f'Bet number {i+1}:', end=" ")
    bet = random.sample(range(1, 61), 6)
    print(sorted(bet))
    time.sleep(2)'''
# now I am going to try to do the same using compounded lists.
from random import randint
from time import sleep
list1 = list()
list2 = list()
total = 1
bet = int(input('How many times do you want to bet? '))
while total <= bet:
    count = 0
    while True:
        numbers = randint(1, 60)
        if numbers not in list1:
            list1.append(numbers)
            count += 1
        if count >= 6:
            break
    list1.sort()
    list2.append(list1[:])
    list1.clear()
    total += 1
print('-='*5, f'Creating {bet} Bets', '-='*5)
for i, l in enumerate(list2):
    print(f'Bet {i+1}: {l}.')
    sleep(1)




