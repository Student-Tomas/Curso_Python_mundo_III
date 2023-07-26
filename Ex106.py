# Challenge number 106: create a mini program that receives a function inserted by the user and return the instructions
# about this function. Include colors and some lines of divisions.

from time import sleep

c = ('\033[m',      # no color
'\033[0;30;41m',    # red
'\033[33;30;42m',    # green
'\033[33;30;43m',    # yellow
'\033[33;30;44m',    # blue
'\033[33;30;45m',    # purple
'\033[7;30m'         # white
     );

def call(com):
    tittle(f'This is the manual of \'{com}\' function:', 4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def tittle(msg, color=0):
    tam = len(msg)
    print(c[color], end='')
    print('~' * (tam + 4))
    print(f'  {msg}')
    print('~' * (tam + 4))
    print(c[0], end='')
    sleep(2)

# Main program
while True:
    tittle('PyHELP SYSTEM', 2)
    comand = str(input('Function or Library: '))
    if comand.strip().upper() == "FIM":
        break
    else:
        call(comand)
tittle('SEE YOU SOON!!!!', 1)
