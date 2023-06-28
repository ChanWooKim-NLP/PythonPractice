from collections import deque

n, k = map(int, input().split())

visited = [-1] * 100001
parent = [-1] * 100001

def bfs():
    queue = deque([n])
    visited[n] = 0
    
    while queue:
        x = queue.popleft()
        
        if x == k:
            # 최단거리 경로를 역추적 후 저장
            path = []
            while x != -1:
                path.append(x)
                x = parent[x]
                
            return path[::-1]
        
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx < 100001 and visited[nx] == -1:
                queue.append(nx)
                visited[nx] = visited[x] + 1
                parent[nx] = x
                
path = bfs()
print(visited[k])
print(*path)