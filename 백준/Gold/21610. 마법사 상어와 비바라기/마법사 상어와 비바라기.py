from collections import deque

n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

move_info = []
for _ in range(m):
    d, s = map(int, input().split())
    
    # 이동 방향 인덱스가 0부터 시작하도록 설정
    move_info.append((d-1, s))

dxs, dys = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 구간이 영역을 벗어나지 않는지 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 이동 후 구름 좌표
def get_next(x, y, d, s):
    return (x + (dxs[d] * s)) % n, (y + (dys[d] * s)) % n

# 대각선에 물이 있는 영역의 개수 찾아 더해주기
def find_water_area_cnt(x, y):
    cnt = 0
    
    diag_dxs, diag_dys = [-1, -1, 1, 1], [-1, 1, -1, 1]
    
    for dx, dy in zip(diag_dxs, diag_dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] > 0:
            cnt += 1
    
    return cnt

cloud_area = deque([(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)])

def move_cloud(d, s):
    # 구름 이동 후 좌표 갱신 및 해당 영역에 물 1씩 더해줌
    for idx in range(len(cloud_area)):
        x, y = cloud_area[idx]
        nx, ny = get_next(x, y, d, s)
        
        # 구름 영역의 물 증가
        arr[nx][ny] += 1
        cloud_area[idx] = (nx, ny)
        
    # 갱신한 물의 양 토대로 대각선 영역 조사 후 구름 제거
    while cloud_area:
        x, y = cloud_area.popleft() # type: ignore
        
        water_area = find_water_area_cnt(x, y)
        arr[x][y] += water_area
        
        # 구름 제거를 방문 배열로 구현
        visited[x][y] = 1

# 2 이상 담긴 물 제거
def remove_water():
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                visited[i][j] = 0
                continue
            
            # 물이 제거된 곳은 새로운 구름
            if arr[i][j] >= 2:
                arr[i][j] -= 2
                cloud_area.append((i, j)) #type: ignore

visited = [
        [0] * n
        for _ in range(n)
    ]

for d, s in move_info:
    move_cloud(d, s)    
    remove_water()
    
ans = 0
for i in range(n):
    for j in range(n):
        ans += arr[i][j]
        
print(ans)