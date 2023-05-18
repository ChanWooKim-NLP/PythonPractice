import sys

input = sys.stdin.readline

n, m = map(int, input().split())

map_arr = [
    input()
    for _ in range(n)
]

arr_idx = [
    [0] * m
    for _ in range(n)
]

idx = 1
for i in range(n):
    for j in range(m):
        arr_idx[i][j] = idx
        idx += 1

parents = [i for i in range(n*m + 1)]

def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    px = find(x)
    py = find(y)
    
    if px > py:
        parents[px] = py
        
    else:
        parents[py] = px

dirs = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
} 

def dfs(x, y):
    idx = arr_idx[x][y]
    
    nx_dir = map_arr[x][y]
    nx, ny = x + dirs[nx_dir][0], y + dirs[nx_dir][1]
    
    n_idx = arr_idx[nx][ny]
    
    if find(idx) != find(n_idx):
        union(idx, n_idx)
    
    else: 
        return
    
    dfs(nx, ny)

for i in range(n):
    for j in range(m):
        dfs(i, j)

print(len(set(parents))-1)