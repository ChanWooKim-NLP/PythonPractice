r, c, t = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(r)
]

# 공기청정기 위치
refresher = 0
for i in range(r):
    if arr[i][0] == -1:
        refresher = i
        break
    
def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

# 확산 불가능한 경우 : 칸을 벗어나거나, 공기청정기가 있는 경우
def can_spread(x, y):
    if not in_range(x, y):
        return False
    
    if arr[x][y] == -1:
        return False
    
    return True

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]


# 1. 미세먼지 확장
def spread_dust():
    # 확산량을 저장할 임시 배열
    temp_spread_arr = [
        [0] * c
        for _ in range(r)
    ]
    
    for x in range(r):
        for y in range(c):
            if arr[x][y] > 0:
                temp_cnt = 0
                
                # 현재 먼지량과 확산량 계산
                cur_dust = arr[x][y]
                spread_amount = cur_dust // 5
                
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    
                    # 인접 칸으로 퍼질 수 있다면
                    if can_spread(nx, ny):
                        temp_spread_arr[nx][ny] += spread_amount
                        temp_cnt += spread_amount
                        
                arr[x][y] -= temp_cnt
    
    for x in range(r):
        for y in range(c):
            arr[x][y] += temp_spread_arr[x][y]
            

def clean_up():
    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
    
    # 이동할 방향
    cur_dir = 0
    
    # 이전 위치 저장할 임시 변수
    # 한 자리씩 뒤로 밀기 때문에 공기청정기 바로 옆은 0이 됨
    temp = 0
    
    # 청소 시작 위치 : 공기청정기 바로 옆
    x, y = refresher, 1
    while True:
        # 공기청정기 자리로 돌아왔다면 탐색 종료
        if (x, y) == (refresher, 0):
            break
        
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        # 벽에 닿았다면 다음 방향으로
        if not in_range(nx, ny):
            cur_dir += 1
            continue
        
        # 현재 위치를 기존 위치의 값으로 바꾸기
        arr[x][y], temp = temp, arr[x][y]
        
        x, y = nx, ny
        
def clean_down():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    cur_dir = 0
    temp = 0
    
    x, y = refresher+1, 1
    while True:
        if (x, y) == (refresher+1, 0):
            break
        
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        
        if not in_range(nx, ny):
            cur_dir += 1
            continue
        
        arr[x][y], temp = temp, arr[x][y]
        
        x, y = nx, ny
        
for _ in range(t):
    spread_dust()
    clean_up()
    clean_down()
    
ans = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            ans += arr[i][j]
            
print(ans)