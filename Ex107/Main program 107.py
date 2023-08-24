# Challenge number 107: create a program, using packeges, that calculates the double, the half, increase and decrease
import currency

number = float(input('What is the number? '))
percent = float(input('What is the percent? '))
print(f'The amount of US$ {number} increased by {percent:.2f}% is US$ {currency.increase(number, percent)}')
print(f'The amount of US$ {number} decreased by {percent:.2f}% is US$ {currency.decrase(number, percent)}')
print(f'The half of US$ {number} is US$ {currency.half(number)}')
print(f'The double of US$ {number} is US$ {currency.double(number)}')

