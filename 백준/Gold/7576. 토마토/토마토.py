import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

storage = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
queue = deque([])


# 초기 토마토 위치 queue에 저장
for i in range(n):
    for j in range(m):
        if storage[i][j] == 1:
            queue.append((i, j, 1))

def bfs():
    global m, n    
    
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
    
    day = 0
    
    while queue:
        x, y, day = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if (0<=nx<n) and (0<=ny<m) and storage[nx][ny] == 0:
                storage[nx][ny] = day+1
                queue.append((nx, ny, day+1))
    
    for i in range(n):
        for j in range(m):
            if storage[i][j] == 0:
                return -1
    
    return day-1

print(bfs())