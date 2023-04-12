from collections import deque

n, k = map(int, input().split())

visited = [float('inf')] * 100001

def in_range(x):
    return 0 <= x < 100001

def bfs(start):
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        x = queue.popleft()
                
        for idx, nx in enumerate((2*x, x-1, x+1)):
            if idx == 0:
                move = 0
                
            else:
                move = 1
            
            if in_range(nx) and visited[x] + move < visited[nx]:
                visited[nx] = visited[x] + move
                queue.append(nx)
                
bfs(n)
print(visited[k])