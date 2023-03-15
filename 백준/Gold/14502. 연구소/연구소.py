import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def wall_build(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall_build(cnt+1)
                arr[i][j] = 0
    
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, arr):
    if not in_range(x, y):
        return False
    
    if arr[x][y] != 0:
        return False
    
    return True

max_safe = 0
def bfs():
    global max_safe
    
    safe_cnt = 0
    queue = deque([])
    
    # 벽을 세우고 시뮬레이션, 원본 배열 유지
    copy_arr = copy.deepcopy(arr)
    
    # 초기 바이러스 위치
    for i in range(n):
        for j in range(m):
            if copy_arr[i][j] == 2:
                queue.append((i, j))

    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
            
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if can_go(nx, ny, copy_arr):
                queue.append((nx, ny))
                copy_arr[nx][ny] = 2
    
    for i in range(n):
        for j in range(m):
            if copy_arr[i][j] == 0:
                safe_cnt += 1
    
    max_safe = max(max_safe, safe_cnt)
    
wall_build(0)

print(max_safe)