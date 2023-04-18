# Challenge number 90: Dice game - Create a program that reades the number of four players and put them in order, using dictionaries
from random import randint
from operator import itemgetter
from time import sleep
data = {'Player1': randint(1, 6),
        'Player2': randint(1, 6),
        'Player3': randint(1, 6),
        'Player4': randint(1, 6)}
print(data)
for k, v in data.items():
    print(f' - {k} got {v}:')
    sleep(1)
ranking = list()
ranking = sorted(data.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('=-' * 30)
for i, v in enumerate(ranking):
    print(f' The {i+1}º place: {v[0]} with {v[1]}')
    sleep(1)
