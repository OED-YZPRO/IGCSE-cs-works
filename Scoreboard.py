inputTeams = input('Enter the team names. ').split()
teamNnR = [['Name']]
def count(results):
    scores = []
    for result in results:
        if result == 'awayWin':
            scores.append(3)
        elif result == 'homeWin':
            scores.append(2)
        elif result == 'draw':
            scores.append(1)
        elif result == 'lost':
            scores.append(0)
    return scores
n = 1 
for team in inputTeams:
    teamNnR.append([team])
    rslt = list(input(f'Enter the results for {team} (homeWin, awayWin, draw, lost). ').split())
    total = 0
    for number in count(rslt):
        teamNnR[n].append(number)
        total += number
    teamNnR[n].append(total)
    n += 1
x = 1
for i in rslt:
    teamNnR[0].append(f'MatchNo{x}')
    x += 1
teamNnR[0].append('total scores')


# print('The scores for each round\n ', teamNnR, '\nNo. of Matches - ', len(teamNnR[1]) - 2)
print('The scores for each round\n')
for rows in teamNnR:
    print(rows)
print('\nNo. of Matches - ', len(teamNnR[1]) - 2)
