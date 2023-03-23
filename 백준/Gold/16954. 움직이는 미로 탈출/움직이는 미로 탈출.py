from collections import deque

maze = deque([
    input() for _ in range(8)
])

def in_range(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if maze[x][y] == '#':
        return False
    
    return True

def bfs(x: int, y: int):
    queue = deque([(x, y)])
    
    wall_down = 0
    dxs, dys = [-1, -1, -1, 0, 1, 1, 1, 0, 0], [-1, 0, 1, 1, 1, 0, -1, -1, 0]
    while queue:
        length_queue = len(queue)
        
        for _ in range(length_queue):
            cur_x, cur_y = queue.popleft()
            
            # 벽이 다 내려오거나, 그 전에 x가 0에 도달했을 땐 방해물이 없음
            if wall_down == 8 or cur_x == 0:
                return True
            
            # 내려오고 나서 현재 위치가 벽이면 다음 좌표 탐색
            if maze[cur_x][cur_y] == '#':
                continue
            
            for dx, dy in zip(dxs, dys):
                nx, ny = cur_x + dx, cur_y + dy
                
                if can_go(nx, ny):
                    queue.append((nx, ny))
        
        # 벽이 내려옴
        maze.pop()
        maze.appendleft('........')
        wall_down += 1
        
    return False

result = bfs(7, 0)

if result:
    print(1)

else:
    print(0)
        