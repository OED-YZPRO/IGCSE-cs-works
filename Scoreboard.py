inputTeams = input('Enter the team names. ').split()
teamNnR = [['Name']]

def check_high_team(team_list):
    high_score = 0
    high_team = ''
    for row in team_list:
      if type(row[-1]) == int and row[-1] > high_score:
        high_score = row[-1]
        high_team = row[0]
    return high_score, high_team
      
def check_low_team(team_list):
    low_score = [1][-1]
    low_team = ''
    for row in team_list:
        if type(row[-1]) == int and row[-1] <= low_score:
            low_score = row[-1]
            low_team = row[0]
    return low_score, low_team

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

highest_score, highest_team = check_high_team(teamNnR)
lowest_score, lowest_team = check_low_team(teamNnR)

print('The scores for each round\n')
for rows in teamNnR:
    print(rows)
print('The highest scoring team ', highest_team)
print('The lowest scoring team ', lowest_team)
print('The highest score ', highest_score)
print('The lowest score ', lowest_score)
print('\nNo. of Matches - ', len(teamNnR[1]) - 2)





