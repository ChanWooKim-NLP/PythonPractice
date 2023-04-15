from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [
        [0] * m
        for _ in range(n)
    ]
    
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
    
    # 범위 확인
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m
    
    # 다음 좌표로 갈 수 있는지 여부
    # 좌표 범위 내 / 방문하지 않은 곳 / 갈 수 있는 곳
    def can_go(x, y):
        if not in_range(x, y):
            return False
        
        if visited[x][y] or maps[x][y] == 'X':
            return False
        
        return True
    
    def bfs(x, y):
        queue = deque([(x, y)])
        
        # 머무를 수 있는 날짜 합
        cnt = 0
        while queue:
            x, y = queue.popleft()
            cnt += int(maps[x][y])
            
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                
                if can_go(nx, ny):
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
        
        return cnt
    
    answer = []
    for i in range(n):
        for j in range(m):
            if can_go(i, j):
                visited[i][j] = 1
                days = bfs(i, j)
                answer.append(days)
    
    if not answer:
        return [-1]
    
    answer.sort()
    return answer