# Challenge number 107: create a program, using packeges, that calculates the double, the half, increase and decrease
import currency

number = float(input('What is the number? '))
percent = float(input('What is the percent? '))
print(f'The number {number} increased by {percent:.1}% is {currency.increase(number, percent)}')


