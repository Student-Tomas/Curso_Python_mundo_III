# Challenge number 096. Make a program that calculates the area of a rectangle using function.
def area(width, heigth):
    a = width * heigth
    print(f'A rectangle with a width of {width} and a height of {heigth} has an area of {a}.')

# Main program
print('='*30)
print('----Terrain Control----')
w = int(input('Say the width: '))
h = int(input('Say the heigth: '))
print('='*30)
area(w, h)
print('='*30)

