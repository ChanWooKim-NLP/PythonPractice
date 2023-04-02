# 미친 아두이노의 이동 방향
# (x1, y1) : 일반 아두이노, (x2, y2) : 미친 아두이노
# 좌표 차이를 Scaling하여 가까운 방향으로 이동하도록 방향 반환
def get_move_dir(x1, y1, x2, y2):
    dir_x = x1 - x2
    dir_y = y1 - y2
    
    # ZeroDivision 방지
    scaler_x = max(abs(dir_x), 1)
    scaler_y = max(abs(dir_y), 1)
    
    # 종수의 아두이노와 가까운 방향으로 이동 
    # 예) x좌표 차이가 -3 / y좌표 차이가 -2이라면 미친 아두이노가 (-1, -1) 이동
    return dir_x // scaler_x, dir_y // scaler_y

def move_normal_arduino(move_idx):
    global arduino
    
    dx, dy = dxs[move_idx], dys[move_idx]
    # 정상 아두이노 이동
    x, y = arduino
    
    nx, ny = x + dx, y + dy
    
    # 미친 아두이노랑 만나면 끝
    if board[nx][ny] == 'R':
        return False
    
    # 새 배열로 아두이노 이동
    new_board[nx][ny] = 'I'
    arduino = (nx, ny)
    
    return True
        
# 방향 순서 인덱스
def move_crazy_arduinos():
    global arduino
    
    # 아두이노가 뭉쳐있는 좌표 목록
    multiple_arduino = set()
    
    # 다른 배열에 기록
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                dx, dy = get_move_dir(arduino[0], arduino[1], i, j)
                
                nx, ny = i + dx, j + dy
                
                # 이동하는 칸 별 조건
                # 종수 아두이노랑 만나면 끝
                if new_board[nx][ny] == 'I':
                    return False
                
                # 다른 미친 아두이노랑 만날 경우 부서짐
                elif new_board[nx][ny] == 'R':
                    multiple_arduino.add((nx, ny))
                    
                # 빈 칸일 경우 이동
                elif new_board[nx][ny] == '.':
                    new_board[nx][ny] = 'R'
    
    # 충돌이 일어난 구간 정리    
    for i, j in list(multiple_arduino):
        new_board[i][j] = '.'
    
    return True
                
r, c = map(int, input().split())

board = []

# 종수의 아두이노 위치
arduino = (-1, -1)
for i in range(r):
    stat_board = list(input())
    board.append(stat_board)
    
    for j in range(c):
        if stat_board[j] == 'I':
            arduino = (i, j)    

move_dir_list = list(input())
move_dir_list = list(map(int, move_dir_list))

# 0번 인덱스는 사용하지 않음
dxs, dys = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1], [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

crashed_idx = 0
crashed = False
for idx, dir_idx in enumerate(move_dir_list):
    # 아두이노들 옮길 새 배열
    new_board = [
        ['.'] * c
        for _ in range(r)
    ]
    
    is_available_normal_move = move_normal_arduino(dir_idx)
    is_available_crazy_move = move_crazy_arduinos()
    
    if not is_available_normal_move or not is_available_crazy_move:
        crashed = True
        crashed_idx = idx+1
        break
    
    # 보드 업데이트
    board = new_board
    
    
if crashed:
    print(f'kraj {crashed_idx}')

else:
    result = ''
    for i in range(r):
        result += ''.join(board[i]) + '\n'
    
    print(result)