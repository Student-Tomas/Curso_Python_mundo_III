# Challenge 095: use the challenge 093 to include as much players as the user want and show the statistics details
team = list()
player = dict()
goals_per_match = list()

while True:
    player.clear()
    player['name'] = str(input('What is the name of the player? '))
    player['matches'] = int(input(f'How many matches has {player["name"]} played? '))
    goals_per_match.clear()
    for x in range(0, player['matches']):
        goals_per_match.append(int(input(f'How many goals in match {x+1} did {player["name"]} score? ')))
    player['goals'] = goals_per_match
    player['total'] = sum(goals_per_match)
    team.append(player.copy())
    while True:
        ask1 = str(input('Do you want to continue? Y or N')).strip().upper()[0]
        if ask1 in "YN":
            break
            print('Error! Please, enter Y or N: ')
        if ask1 == "N":
            break





    '''print('~-~'*30)
    print(player)
    print('-='*30)
    for k, v in player.items():
        print(f'The item {k} has the information {v}.')
    print('=-'*30)
    print(f'The player {player["name"]} played {len(goals_per_match)} matches, and scored a total of {player["total"]} goals.')
    for m, g in enumerate(goals_per_match):
        print(f'In the match number {m+1} the player {player["name"]} scored {g} goals.')'''

