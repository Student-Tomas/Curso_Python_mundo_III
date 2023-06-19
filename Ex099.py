# Challenge 099: creat a function to find out which number is the biggest and how many numbers were informed.

from time import sleep

def num_informed(* number):
    cont = biggest = 0
    print('-='*30)
    print(f'The numbers informed were: ')
    for value in number:
        print(f'{value}', end=" ")
        sleep(0.3)
        if cont == 0:
            biggest = value
        else:
            if value > biggest:
                biggest = value
        cont += 1
    print(f'\n{cont} numbers were informed')
    print(f'The biggest is {biggest}')


# Main program
num_informed(8, 4, 9, 9, 3, 2, 10)
num_informed(2, 1, 3)
num_informed(11, 3, 4, 5)
num_informed(1, 2)
num_informed(3)
num_informed()