# Challenge number 104: creat a function that works like the input builtin function
# include data validation in order to receive only integers numbers
def read_int(number):
    print(f'The number inserted by the user was: {number}')


# Main program
n = str(input('Insert an integer number: '))
if n.isnumeric():
    n = int(n)
elif n.isalpha():
    while True:
        print(f'\033[0:31mError! insert only numbers.\033[m')
        n = str(input('Insert an integer number: '))
        if n.isnumeric():
            break
elif n.strip() == "":
    n = 'none'
read_int(n)

