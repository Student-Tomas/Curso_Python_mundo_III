# Challenge number 090? make a program that reads the name and grade of a student in a dictionary
# besides this, includes the final situation of the student in this same dictionary.
name = str(input('Name: '))
grade = float(input('Grade: '))
data = {}
data['name'] = name
data['grade'] = grade
if grade >= 7:
    situation = 'approved'
else:
    situation = 'disapproved'
data['situation'] = situation
print(data)
for k, v in data.items():
    print(f' The {k} is {v}.')

