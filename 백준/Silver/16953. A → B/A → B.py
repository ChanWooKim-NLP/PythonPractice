from collections import deque

a, b = map(int, input().split())

visited = {}

def bfs(n):
    queue = deque([n])
    visited[n] = 1
    
    while queue:
        n = queue.popleft()
        
        if n == b:
            return visited[b]
        
        for next_n in (n*2, n*10+1):
            if 1 <= next_n <= b and next_n not in visited.keys():
                queue.append(next_n)
                visited[next_n] = visited[n] + 1
                
    return -1

result = bfs(a)

print(result)