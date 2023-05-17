import sys
from collections import defaultdict

# 상어가 이동하는 함수
def _move_shark(cur_r, cur_c, speed, direction):
    global r, c
    
    move_cnt = speed
    cur_direction = direction

    while move_cnt > 0:
        # 바라보는 방향으로 이동해야 하는 칸 수
        if cur_direction == 1: move = cur_r - 1
        elif cur_direction == 2: move = r - cur_r
        elif cur_direction == 3: move = c - cur_c
        else: move = cur_c - 1
        
        if move_cnt <= move:
            move = move_cnt
            
        nr, nc = cur_r + move*dxs[cur_direction], cur_c + move*dys[cur_direction]
        
        cur_r, cur_c = nr, nc
        move_cnt -= move
        
        if move_cnt > 0:
            if cur_direction in [1, 3]:
                cur_direction += 1
                
            else:
                cur_direction -= 1
            
    return cur_r, cur_c, cur_direction

# 낚시꾼이 땅을 이동하며 먼저 낚는 상어를 잡는 함수
def catch_shark(move_idx):
    global r, c
    
    shark_idx = 0
    for row in range(1, r+1):
        shark_idx = arr[row][move_idx]
        # 상어를 잡으면 배열에서 제거
        if shark_idx > 0:
            arr[row][move_idx] = 0
            break
    
    # 해당 열에 잡히는 상어가 없다면 0 반환
    if shark_idx == 0:
        return 0
    
    size = shark_dict[shark_idx][-1]
    
    # 딕셔너리에서 제거
    shark_dict.pop(shark_idx)
    return size
    
# 단일 상어의 움직임을 나타내는 함수
def move_sharks(shark_idx):
    global r, c
    
    cur_r, cur_c, speed, direction, size = shark_dict[shark_idx]
    
    nx_r, nx_c, n_dir = _move_shark(cur_r, cur_c, speed, direction)
    
    # 새로운 좌표에 상어를 이동 
    # 이동 후 같은 좌표를 가질 수 있음
    # 또한, 떠난 자리에 이미 다른 상어가 있을 가능성
    new_arr[nx_r][nx_c] = shark_idx

    # 상어 정보 업데이트
    shark_dict[shark_idx] = [nx_r, nx_c, speed, n_dir, size]
    
    # 이동이 끝난 후 딕셔너리에 이동 후 좌표를 key로, 상어 번호와 사이즈 저장
    all_shark_after_move[(nx_r, nx_c)].append([shark_idx, size])
    return

# 이동 후 같은 좌표에 있는 상어를 확인하고 잡아먹는 함수
def kill_shark_in_same_coordinate():
    for key, value in all_shark_after_move.items():
        if len(value) >= 2:
            # 사이즈 기준 내림차순 정렬
            value.sort(key=lambda x: -x[1])
            biggest_shark_idx = value[0][0]
            new_arr[key[0]][key[1]] = biggest_shark_idx
            
            # 가장 큰 상어를 제외한 나머지 상어들은 잡아먹혔으므로 상어 정보에서 제거
            for idx in range(1, len(value)):
                shark_idx = value[idx][0]
                shark_dict.pop(shark_idx)
                
input = sys.stdin.readline

r, c, m = map(int, input().split())

arr = [
    [0] * (c+1)
    for _ in range(r+1)
]

shark_dict = {}
shark_list = []
for idx in range(1, m+1):
    x, y, s, d, z = map(int, input().split())
    arr[x][y] = idx
    shark_dict[idx] = [x, y, s, d, z]
    
    # 처음에 존재한 상어 번호
    shark_list.append(idx)

# 1번 인덱스부터 사용하는 방향 리스트
# 1, 2 : 위 / 아래
# 3, 4 : 오른쪽 / 왼쪽
dxs, dys = [0, -1, 1, 0, 0], [0, 0, 0, 1, -1]

answer = 0
# 낚시꾼이 땅을 한 칸 옆으로 이동
move_idx = 1
while move_idx <= c:
    if m == 0:
        break
    
    # 모든 상어의 이동 후 정보
    all_shark_after_move = defaultdict(list)
    
    size = catch_shark(move_idx)
    answer += size
    
    new_arr = [
        [0] * (c+1)
        for _ in range(r+1)
    ]
    
    # 각 번호의 상어가 이동
    for shark_idx in shark_list:
        # 해당 번호의 상어가 안잡아먹히고 아직 살아있다면 이동 수행
        is_alive = shark_dict.get(shark_idx, False)
        if is_alive:
            move_sharks(shark_idx)
    
    kill_shark_in_same_coordinate()
    move_idx += 1
    
    arr = new_arr
    
print(answer)