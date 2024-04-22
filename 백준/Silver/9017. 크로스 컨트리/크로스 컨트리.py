import sys
from collections import defaultdict, Counter

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    teams = list(map(int, sys.stdin.readline().split()))
    
    team_people = Counter(teams)
    result = defaultdict(list)
        
    rank = 1
    for mem in teams:
        if team_people[mem] < 6:
            continue
        
        else:
            if len(result[mem]) < 5:
                result[mem].append(rank)
                                    
            rank += 1
    
    answer = []
    for team in result:
        final = result[team]
        answer.append((sum(final[:4]), final[4], team))
    
    answer.sort(key=lambda x: (x[0], x[1]))
    
    print(answer[0][-1])