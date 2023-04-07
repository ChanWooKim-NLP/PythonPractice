from collections import deque

m, n = map(int, input().split())

maze = [
    input()
    for _ in range(n)
]

visited = [
    [-1] * m
    for _ in range(n)
]

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny) and visited[nx][ny] == -1:
                # 벽이 아니라면 해당 구간까지 오는데 깬 벽의 수를 기록
                if maze[nx][ny] == '0':
                    visited[nx][ny] = visited[x][y]
                    
                    # 벽이 없는 공간부터 먼저 탐색하도록 우선권 조정 
                    #   -> 목적지까지 벽을 깨는 횟수 최소화
                    queue.appendleft((nx, ny))
                
                # 벽을 깬 수 +1                    
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    
                    # 벽이 있는 구역은 큐의 뒤에 삽입
                    queue.append((nx, ny))
    return

bfs(0, 0)
print(visited[-1][-1])
