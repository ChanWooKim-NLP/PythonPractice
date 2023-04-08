from collections import deque
from pprint import pprint

n = int(input())

k = int(input())

arr = [
    [0] * n
    for _ in range(n)
]

for _ in range(k):
    # 사과의 위치 기록
    apple_r, apple_c = map(int, input().split()) 
    arr[apple_r-1][apple_c-1] = 1
    
direct_list = deque([])

l = int(input())
for _ in range(l):
    x, c = input().split()
    x = int(x)
    
    direct_list.append((x, c))

# 시계 방향 순 이동 좌표
# 방향 전환 타이밍 때 L, D 방향으로 전환
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 배열 안 뱀의 몸 위치
visited = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 이동 가능 여부, 불가능하다면 게임 끝
def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y]:
        return False
    
    return True

# 방향 전환 함수
# 현재 향하는 방향에서 convert (L/D)
def convert_dir(cur_dir, convert):
    if convert == 'D':
        cur_dir = (cur_dir + 1) % 4
        
    else:
        cur_dir = (cur_dir - 1) % 4
        
    return cur_dir

def bfs(x, y):
    # 
    queue = deque([(x, y)])
    
    visited[x][y] = 1
    
    cur_dir = 0
    time = 0
    while True:
        x, y = queue[0]
        
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        if can_go(nx, ny):
            # 시간 증가
            time += 1
            
            # 사과가 아닌 경우는 queue의 top -> 꼬리 제거
            if arr[nx][ny] == 0:
                tail_x, tail_y = queue.pop()
                visited[tail_x][tail_y] = 0
            
            # 사과를 먹었으므로 제거
            else:
                arr[nx][ny] = 0
            
            # 머리 좌표 추가
            visited[nx][ny] = 1
            queue.appendleft((nx, ny))
            
            # X초가 지나면 방향 전환
            if direct_list and direct_list[0][0] == time:
                _, convert = direct_list.popleft()
                cur_dir = convert_dir(cur_dir, convert)
        
        # 지나갈 수 없는 경우, 시간 증가하고 게임 끝
        else:
            return time + 1
        
ans = bfs(0, 0)
print(ans)