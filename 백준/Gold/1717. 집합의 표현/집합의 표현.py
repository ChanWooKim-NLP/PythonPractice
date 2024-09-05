import sys
sys.setrecursionlimit(1000000)


n, m = map(int, sys.stdin.readline().split())

parents = [i for i in range(n+1)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    
    return parents[x]

def union(x, y):
    parent_x = find(x)
    parent_y = find(y)
    
    if parent_x > parent_y:
        parents[parent_x] = parent_y
        
    else:
        parents[parent_y] = parent_x

for _ in range(m):
    t, a, b = map(int, sys.stdin.readline().split())
    
    if t == 0:
        union(a, b)
        
    else:
        if find(a) == find(b):
            print('YES')
            
        else:
            print('NO')