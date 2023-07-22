import sys

input = sys.stdin.readline

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

n, m = map(int, input().split())

graph = []

total_cost = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
    
    total_cost += c

graph.sort(key=lambda x: x[-1])

parents = [i for i in range(n+1)]

buildings = 1
cost = 0
for x, y, c in graph:
    if buildings == n:
        break
    
    if find(x) != find(y):
        union(x, y)
        buildings += 1
        cost += c
        
if buildings == n:
    print(total_cost - cost)
    
else:
    print(-1)