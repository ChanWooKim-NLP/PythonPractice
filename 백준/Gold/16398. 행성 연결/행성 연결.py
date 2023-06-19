import sys

input = sys.stdin.readline

n = int(input())
flow = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 두 정점 간 관리 비용
costs = []
for i in range(n):
    for j in range(i+1, n):
        costs.append((i, j, flow[i][j]))

costs.sort(key=lambda x: x[-1])

parents = [i for i in range(n)]

def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]        

def union(x, y):
    px, py = find(x), find(y)
    
    if px > py:
        parents[px] = py
        
    else:
        parents[py] = px
        
answer = 0
for i, j, cost in costs:
    if find(i) != find(j):
        union(i, j)
        answer += cost
        
print(answer)