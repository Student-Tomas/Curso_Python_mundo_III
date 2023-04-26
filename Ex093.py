#Challenge number 093: use a dictionary to show some estatistics about a soccer player
all_data = dict()
all_data['name'] = str(input('What is the name of the player? '))
all_data['matches'] = int(input(f'How many matches has {all_data["name"]} played? '))
goals_per_match = list()
print('=-'*30)
for x in range(0, all_data['matches']):
    goals_per_match.append(int(input(f'How many goals in match {x+1} did {all_data["name"]} score? ')))
all_data['goals'] = goals_per_match
all_data['total'] = sum(goals_per_match)
print('~-~'*30)
print(all_data)
print('-='*30)
for k, v in all_data.items():
    print(f'The item {k} has the information {v}.')
print('=-'*30)
print(f'The player {all_data["name"]} played {len(goals_per_match)} matches, and scored a total of {all_data["total"]} goals.')
for m, g in enumerate(goals_per_match):
    print(f'In the match number {m+1} the player {all_data["name"]} scored {g} goals.')
