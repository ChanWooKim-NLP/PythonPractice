import sys
from collections import deque

input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# bfs를 하면서 녹아야 함
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        around_sea_arr[x][y] = 0
                
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny) and not visited[nx][ny]:
                if iceberg[nx][ny] != 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    
                elif iceberg[nx][ny] == 0:
                    around_sea_arr[x][y] += 1
                    
n, m = map(int, input().split())

iceberg = [
    list(map(int, input().split()))
    for _ in range(n)
    ]

# 주변 바닷물 영역 저장 배열
around_sea_arr = [
        [0] * m
        for _ in range(n)
    ]

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

# 인접한 바닷물 구간을 구하고, 빙하를 녹이는 메소드
year = 0
while True:
    # 탐색 횟수
    cnt = 0
    visited = [
            [0] * m
            for _ in range(n)
            ]

    # 탐색 가능한 빙산이 존재하는지 여부
    # 배열이 모두 0이라면 False    
    for i in range(1, n-1):
        for j in range(1, m-1):
            if not visited[i][j] and iceberg[i][j] != 0:
                # 탐색하였으므로 횟수 증가
                bfs(i, j)
                cnt += 1
    
    for i in range(1, n-1):
        for j in range(1, m-1):
            iceberg[i][j] -= around_sea_arr[i][j]
            
            if iceberg[i][j] < 0:
                iceberg[i][j] = 0       
    
    if cnt >= 2:
        break
    
    if cnt == 0:
        year = 0
        break
    
    year += 1
    
print(year)
    