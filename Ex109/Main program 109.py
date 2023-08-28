# Challenge number 107: create a program, using packages, that calculates the double, the half, increase and decrease
from Ex109 import currency

number = float(input('What is the number? '))
percent = float(input('What is the percent? '))
print(f'The amount of {currency.currency(number)} increased by {percent}% is {currency.increase(number, percent, True)}')
print(f'The amount of {currency.currency(number)} decreased by {percent:.2f}% is {currency.decrease(number, percent, True)}')
print(f'The half of {currency.currency(number)} is {currency.half(number, True)}')
print(f'The double of {currency.currency(number)} is  {currency.double(number, True)}')

