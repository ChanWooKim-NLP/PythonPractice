from collections import defaultdict

n, g = input().split()

n = int(n)

minimum_player = {'Y' : 1, 'F' : 2, 'O' : 3}

players = defaultdict(int)
for _ in range(n):
    player = input()
    players[player] += 1
    
answer = len(players.keys()) // minimum_player[g]
print(answer)