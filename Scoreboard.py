inputTeams = input('Enter the team names. ').split()
teamNnR = [['Name: ']]
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
            scores.append(2)
n = 1 
    for item in inputTeams:
        rslt = list(input(f'Enter the results for {team} (homeWin, awayWin, draw, lost). ').split())
        teamNnR.append([team])
        for number in count(rslt):
            teamNnR[n].append(number)
        n += 1
x = 1
    for i in rslt:
        teamNnR[0].append(f'MatchNo{x}')
        x += 1
print('The scores for each round\n ', teamNnR, '\nNo. of Matches - ', x)
