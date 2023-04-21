r, c = map(int, input().split())

arr = [
    list(input())
    for _ in range(r)
]

# 이동 방향은 하나로 고정
# 파이프 별 방향 전환

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

# 1번부터 4번 파이프는 입구 방향에 따라 진출 방향이 달라짐
def pipe_1(move_idx):
    if move_idx == 0: move_idx = (move_idx + 1) % 4 # 0 -> 1
    elif move_idx == 3: move_idx = (move_idx - 1) % 4 # 3 -> 2
    return move_idx

def pipe_2(move_idx):
    if move_idx == 2: move_idx = (move_idx - 1) % 4 # 2 -> 1
    elif move_idx == 3: move_idx = (move_idx + 1) % 4 # 3 -> 0
    return move_idx

def pipe_3(move_idx):
    if move_idx == 1: move_idx = (move_idx - 1) % 4 # 1 -> 0
    elif move_idx == 2: move_idx = (move_idx + 1) % 4 # 2 -> 3
    return move_idx

def pipe_4(move_idx):
    if move_idx == 1: move_idx = (move_idx + 1) % 4 # 1 -> 2
    elif move_idx == 0: move_idx = (move_idx - 1) % 4 # 0 -> 3
    return move_idx

# 자그레브와 모스크바 위치
zagrev = (-1, -1)
moscow = (-1, -1)
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'M':
            moscow = (i, j)
            
        elif arr[i][j] == 'Z':
            zagrev = (i, j)

# 초기 연결 파이프 탐색 시 범위 내에서 탐색하기 위한 함수
def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

def find_cut_corr(start):
    x, y = start
    move = -1
    
    # 시작점 주변에 연결된 파이프를 찾아 초기 이동 방향으로 설정
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        
        if in_range(nx, ny) and arr[nx][ny] != '.':
            move = i

    # 가스의 흐름은 유일함, 더 이상 갈 수 없을 경우 반복문 탈출
    while True:
        # 이동지가 끊긴 파이프라면 좌표와 방향 반환
        if arr[x][y] == '.':
            return x, y, move
        
        # 현재 위치 x와 y의 파이프 종류 탐색, 1~4 중 하나라면 방향 전환
        if arr[x][y] == '1': move = pipe_1(move)
        elif arr[x][y] == '2': move = pipe_2(move)
        elif arr[x][y] == '3': move = pipe_3(move)
        elif arr[x][y] == '4': move = pipe_4(move)
        
        nx, ny = x + dxs[move], y + dys[move]
        x, y = nx, ny

# 끊긴 파이프 기준 모스크바에서 자그레브로 호르는 
def find_cut_pipe(from_dir, to_dir):
    # 방향이 0이나 2로 같을 경우
    if from_dir == to_dir == 2 or from_dir == to_dir == 0:
        return '|'
    
    # 1과 3으로 같을 경우
    if from_dir == to_dir == 1 or from_dir == to_dir == 3:
        return '-'
    
    if pipe_1(from_dir) == to_dir:
        return '1'
    
    if pipe_2(from_dir) == to_dir:
        return '2'
    
    if pipe_3(from_dir) == to_dir:
        return '3'
    
    if pipe_4(from_dir) == to_dir:
        return '4'

# 4방향 연결 모두 가능한 십자 파이프 확인
def find_cross(x, y):    
    # 어느 방향으로 흐를 수 있는지 확인하는 리스트
    can_go = [0] * 4
    
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        
        if in_range(nx, ny) and arr[nx][ny] != '.':
            if i == 0 and arr[nx][ny] in ('1', '4', '|', '+'):
                can_go[i] = 1
                
            elif i == 1 and arr[nx][ny] in ('3', '4', '-', '+'):
                can_go[i] = 1
                
            elif i == 2 and arr[nx][ny] in ('2', '3', '|', '+'):
                can_go[i] = 1
                
            elif i == 3 and arr[nx][ny] in ('1', '2', '-', '+'):
                can_go[i] = 1
    
    return can_go

# 1. 모스크바에서 끊긴 파이프와 향하고 있는 방향 확인
cut_x, cut_y, m_move = find_cut_corr(moscow)

# 2. 자그레브에서 이동 방향 확인 후 180도 회전
_, _, z_move = find_cut_corr(zagrev)
z_move = (z_move + 2) % 4

# 잘린 파이프 위치 기준 4면에 모두 연결 가능한 파이프가 있을 경우 '+'
interlink_arr = find_cross(cut_x, cut_y)

is_cross = True
for i in range(4):
    if interlink_arr[i] == 0:
        is_cross = False
        break

if is_cross:
    pipe = '+'

else:
    pipe = find_cut_pipe(m_move, z_move)
    
print(cut_x+1, cut_y+1, pipe)