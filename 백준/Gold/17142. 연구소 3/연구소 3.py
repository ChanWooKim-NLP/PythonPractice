import sys
from collections import deque
from itertools import combinations

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, visited):
    if not in_range(x, y):
        return False
    
    if visited[x][y] >= 0 or arr[x][y] == 1:
        return False
    
    return True    

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

# 전체 바이러스의 위치 목록
virus_locations = []
for i in range(n):
    lab = list(map(int, input().split()))
    
    for j in range(n):
        if lab[j] == 2:
            virus_locations.append((i, j))

    arr.append(lab)
    
def check_all_filled(visited):
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and arr[i][j] == 0:
                return False
            
    return True


# 바이러스 m개 선택
selected_virus_list = list(combinations(virus_locations, m))
def bfs(selected_virus):
    visited = [
        [-1] * n
        for _ in range(n)
        ]
    
    # 초기 시작 좌표 시간 0으로 설정
    for i, j in selected_virus:
        visited[i][j] = 0
    
    queue = deque(list(selected_virus))
    
    max_spread_time = 0
    
    # bfs 수행
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
                
            # 다음 좌표로 갈 수 있는 경우
            if can_go(nx, ny, visited):                
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                
                # 원래 빈칸일 경우에 확산 시간을 갱신함
                # 비활성 바이러스에 닿으면 그 순간 활성으로 변하기 때문
                if arr[nx][ny] == 0:
                    max_spread_time = max(max_spread_time, visited[nx][ny])

    
    if check_all_filled(visited):
        return max_spread_time
    
    else:
        return -1

# 모든 활성 바이러스 조합 별로 bfs 수행
# 각 경우 별 최대 확장 시간을 구하고 지금까지 구한 최소 시간하고 비교
answer = 1e9
for selected_virus in selected_virus_list:
    max_spread_time = bfs(selected_virus)
    
    if max_spread_time != -1:
        answer = min(answer, max_spread_time)

# 갱신이 안될 경우
if answer == 1e9: 
    print(-1)
    
else: print(answer)