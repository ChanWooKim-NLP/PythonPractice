from collections import deque
from pprint import pprint

n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, not_go):
    if not in_range(x, y):
        return False
    
    if visited[x][y] or arr[x][y] == not_go:
        return False
    
    return True

# 외부 공기 구간 탐색
def bfs_air(x, y, not_go=1):
    queue = deque([(x, y)])
    
    # 모눈종이 가장자리는 공기
    visited[x][y] = -1
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            # 치즈 주변 공기 탐색, 외부 공기는 -1로 표시
            if can_go(nx, ny, not_go):
                visited[nx][ny] = -1
                queue.append((nx, ny))


time = 0
while True:
    visited = [
        [0] * m
        for _ in range(n)
    ]
    
    # 배열에 존재하는 전체 치즈 크기
    total_cheese_cnt = 0
    
    # 외부 공기 탐색
    bfs_air(0, 0, 1)

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                visited[i][j] = 1
    
    # visited 배열에 기록한 외부 공기와 치즈 여부로 인접한 외부 공기 수 계산
    for i in range(1, n-1):
        for j in range(1, m-1):
            # 2칸 이상 인접하면 치즈 제거
            arround_air = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                
                if visited[nx][ny] == -1:
                    arround_air += 1
            
            if arround_air >= 2:
                arr[i][j] = 0

            # 제거 후 치즈 더하기
            total_cheese_cnt += arr[i][j]

    time += 1
    
    # 제거 후 치즈가 남아있지 않다면 끝
    if total_cheese_cnt == 0:
        break
    
print(time)