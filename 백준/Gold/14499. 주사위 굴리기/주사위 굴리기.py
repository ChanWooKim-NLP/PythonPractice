from collections import deque

n, m, x, y, k = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 순서
order = list(map(int, input().split()))

# 주사위 단면, 1: 동쪽, 2: 서쪽, 3: 북쪽, 4: 남쪽
# 바닥을 기준으로 동서북남
# 현재 바닥과 윗면 저장
dice = [0, 0, 0, 0]
cur_bottom = 0
cur_top = 0

# 바닥과 윗면의 관계, 동쪽으로 방향을 틀면 서쪽이 윗면으로 옴
top_dict = {
    0 : 1,
    1 : 0,
    2 : 3,
    3 : 2
}

# 범위 내 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 이동 방향, 인덱스 별로 동서북남
dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

# 명령의 수 만큼 이동 수행
for idx in range(k):
    # 이동할 방향 인덱스
    direction = order[idx] - 1
    nx, ny = x + dxs[direction], y + dys[direction]
    
    # 이동이 가능하다면
    if in_range(nx, ny):
        # 기존 바닥과 윗면은 이동 방향에 따라 바닥과 이웃한 4개의 면에 새로 기록
        # 동/서로 움직일 시, 남/북의 값은 변하지 않으며, 반대도 마찬가지
        # top_dict을 통해 이동한 면과 반대에 있는 면을 같이 갱신
        prev_bottom = cur_bottom
        prev_top = cur_top
        
        # direction으로 이동했을 때 새로운 바닥과 윗면 
        cur_bottom = dice[direction]
        cur_top = dice[top_dict[direction]]
        
        # 주사위 갱신
        dice[direction] = prev_top
        dice[top_dict[direction]] = prev_bottom
        
        # 답안 출력
        print(cur_top) 
        
        # 배열의 값에 따라 복사 진행
        arr_val = arr[nx][ny]
        if arr_val == 0:
            arr[nx][ny] = cur_bottom
            
        else:
            cur_bottom = arr_val
            arr[nx][ny] = 0
        
        # 좌표 갱신
        x, y = nx, ny
        
        
        
        
            