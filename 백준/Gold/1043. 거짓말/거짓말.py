from collections import deque, defaultdict

n, m = map(int, input().split())

cnt = list(map(int, input().split()))
truth_know = []

if cnt[0] != 0:
    truth_know = cnt[1:]
    
graph = defaultdict(list)

party_list = []
for _ in range(m):
    party = list(map(int, input().split()))
    participation = party[1:]
    party_list.append(participation)
    
    # 그래프
    if party[0] != 1:
        for i in range(len(participation)-1):
            for j in range(i+1, len(participation)):
                if participation[j] not in graph[participation[i]]:
                    graph[participation[i]].append(participation[j])
                    graph[participation[j]].append(participation[i])

visited = [0] * (n+1)
def bfs(x):
    visited[x] = 1
    
    for node in graph[x]:
        if not visited[node]:
            bfs(node)
            
if cnt[0] == 0:
    print(m)
    
else:
    answer = m
    for know in truth_know:
        bfs(know)
    
    know = []
    for i in range(1, len(visited)):
        if visited[i] == 1:
            know.append(i)
    
    
    for party in party_list:
        for p_idx in know:
            if p_idx in party:
                answer -= 1
                break
            
    print(answer)