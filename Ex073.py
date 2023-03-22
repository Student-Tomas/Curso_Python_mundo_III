# Challenge number 072: Say the top five teams and the botton four. Also put them in alphabetc order and say the "Coritiba's" position.
teams = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico_Paranaense', 'Atlético_Mineiro', 'Fortaleza',
'São_Paulo', 'América', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético_GO', 'Avaí', 'Juventude')
print('~~'*30)
print(f'The top five are: {teams[:5]}')
print('~~'*30)
print(f'The botton four are: {teams[-4:]}')
print('~~'*30)
print(f'This group in alphabetic order is: {sorted(teams)}')
print('~~'*30)
print(f'The Coritiba is in {teams.index("Coritiba")+1}th position')
print('~~'*30)
print(f'We have {len(teams)} teams in this list')




