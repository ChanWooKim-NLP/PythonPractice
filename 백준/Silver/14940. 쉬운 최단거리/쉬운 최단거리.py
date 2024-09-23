import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

arr = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

visited = [
    [-1] * m
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if arr[x][y] == 0 or visited[x][y] >= 0:
        return False
    
    return True

def dfs(sx, sy):
    queue = deque([(sx, sy)])
    visited[sx][sy] = 0
    
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if can_go(nx, ny):
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
        
        
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            dfs(i, j)
            break
        
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=' ')
        
        else:
            print(visited[i][j], end=' ')
    print()