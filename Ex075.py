# Challenge number 075: create a program that reads four numbers and store them in a tuple. After that, say how many times
# the number nine appears, in which position the number three appeared for the first time, and what were the evem numbers.
my_tuple = (int(input('number one: ')),
            int(input('number two: ')),
            int(input('number three: ')),
            int(input('number four: ')))
print('~~'*30)
print(my_tuple)
print('~~'*30)
print(f'We have {my_tuple.count(9)} numbers nine')
print('~~'*30)
if 3 in my_tuple:
    print(f'The number three appeared for the first time in {my_tuple.index(3)+1} position')
else:
    print(f'There is no number three.')
print('~~'*30)
even_list = []
even_counter = 0
for i in my_tuple:
    if i % 2 == 0:
        even_counter += 1
        even_list.append(i)
print(f'We have {even_counter} even numbers, and they are: ', end=" ")
print(even_list)






