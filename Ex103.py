"""# Challenge number 103: create a function called "form" that receives the name of a player and how many goals
# did he or she scored. If some information was not inserted, show unknown for the name and zero for gols.
def form(player='<unknown>', goals=0):
    print(f'The player {player} scored {goals} goals.')


# Main Program
p = str(input("What is the name of the player? "))
g = str(input("How many goals did the player scored? "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if p.strip() == '':
    form(goals=g)
else:
    form(p, g)
"""
# another try:
def form(player='<Unknon>', goals=0):
    print(f'The player {player} scored {goals} goals this season.')

# Main program
p = str(input('What is the name of the player? '))
g = str(input('How many goals the player socred? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if p.strip() == "":
    form(goals=g)
else:
    form(p, g)

