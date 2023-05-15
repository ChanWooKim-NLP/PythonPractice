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

parents = [i for i in range(n)]

points = []
for _ in range(m):
    a, b = map(int, input().split())
    points.append((a, b))

answer = 0
for idx, (a, b) in enumerate(points):
    if find(a) != find(b):
        union(a, b)
        
    else:
        answer = idx + 1
        break
    
print(answer)