from collections import deque

n, m = map(int, input().split())

arr = [
    input()
    for _ in range(n)
]

# 0 : 벽을 뚫지 않음 / 1 : 벽을 뚫고 이동함
visited = [
    [[0 for _ in range(2)]
    for _ in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y, 0)])
    
    while queue:
        # destroy : 0 / 1 
        # 0 : 벽을 부수지 않은 경우 / 1 : 벽을 부수고 지나간 경우
        x, y, destroy = queue.popleft()
        
        if x == n-1 and y == m-1:
            return visited[x][y][destroy]
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny):
                # 이동할 칸이 벽이고 아직 벽을 부수지 않았을 경우
                # 벽을 1번 부셨으므로 방문 배열의 [nx][ny][1]에 방문 표사
                if arr[nx][ny] == '1' and destroy == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
                
                # 벽이 아니고, 아직 방문하지 않았을 경우
                elif arr[nx][ny] == '0' and visited[nx][ny][destroy] == 0:
                    visited[nx][ny][destroy] = visited[x][y][destroy] + 1
                    queue.append((nx, ny, destroy))
                    
    return -1

visited[0][0][0] = 1
print(bfs(0, 0))