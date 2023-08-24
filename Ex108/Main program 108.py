# Challenge number 107: create a program, using packages, that calculates the double, the half, increase and decrease
from Ex108 import currency

number = float(input('What is the number? '))
percent = float(input('What is the percent? '))
print(f'The amount of {currency.currency(number)} increased by {percent}% is {currency.currency(currency.increase(number, percent))}')
print(f'The amount of {currency.currency(number)} decreased by {percent:.2f}% is {currency.decrease(number, percent)}')
print(f'The half of {currency.currency(number)} is {currency.currency(currency.half(number))}')
print(f'The double of {currency.currency(number)} is  {currency.currency(currency.double(number))}')

