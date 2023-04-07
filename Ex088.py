# Challenge number 088: create a program that gives sugestions to bet in the lotery.
# six different random numbers from zero to sixty, how many times the user want.
import random, time
num = int(input('How many times do you want to bet? '))
for i in range(0, num):
    print(f'Bet number {i+1}:', end=" ")
    bet = random.sample(range(1, 61), 6)
    print(sorted(bet))
    time.sleep(2)


