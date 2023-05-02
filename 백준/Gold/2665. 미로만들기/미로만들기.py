from collections import deque

n = int(input())

maze = [
    list(input())
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n



def bfs():
    visited = [
        [float('inf')] * n
        for _ in range(n)
    ]
       
    queue = deque([(0, 0)])
    
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
    visited[0][0] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny):
                if visited[nx][ny] <= visited[x][y]:
                    continue
                
                if maze[nx][ny] == '0':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    
                elif maze[nx][ny] == '1':
                    visited[nx][ny] = visited[x][y]
                    queue.append((nx, ny))
                    
    return visited

visited = bfs()
print(visited[-1][-1])