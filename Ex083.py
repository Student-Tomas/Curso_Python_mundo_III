# Challenge number 083: create a program that check if the mathematic expression is valid in terms of brackets.
expression = str(input('Enter the expression: '))
pile = []
for simbol in expression:
    if simbol == '(':
        pile.append('simbol')
    elif simbol == ')':
        if len(pile) > 0:
            pile.pop()
        else:
            pile.append(')')
            break
if len(pile) == 0:
    print('The expression is correct!')
else:
    print('The expression is incorrect!')
