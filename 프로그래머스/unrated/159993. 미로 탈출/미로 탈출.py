from collections import deque

def solution(maps):
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m
    
    def can_go(x, y, visited):
        if not in_range(x, y):
            return False
        
        if visited[x][y] or maps[x][y] == 'X':
            return False
        
        return True
    
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
    
    def bfs(x, y, target_x, target_y):
        visited = [
            [0] * m
            for _ in range(n)
        ]
        
        visited[x][y] = 1
        queue = deque([(x, y, 0)])
        
        while queue:
            x, y, cnt = queue.popleft()
            
            if x == target_x and y == target_y:
                return cnt
            
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                
                if can_go(nx, ny, visited):
                    visited[nx][ny] = 1
                    queue.append((nx, ny, cnt+1))
        
        return -1
        
    answer = 0
    
    n, m = len(maps), len(maps[0])
    start, end, lever = 0, 0, 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            
            elif maps[i][j] == 'E':
                end = (i, j)
                
            elif maps[i][j] == 'L':
                lever = (i, j)
    
    s_to_l = bfs(start[0], start[1], lever[0], lever[1])
    l_to_e = bfs(lever[0], lever[1], end[0], end[1])
    
    if s_to_l == -1 or l_to_e == -1:
        return -1
    
    answer = s_to_l + l_to_e
                
    return answer