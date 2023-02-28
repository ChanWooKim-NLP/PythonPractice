from collections import deque

n, k = map(int, input().split())

arr = [0] * 100001

visited = [0] * 100001

def bfs(x):    
    if x == k:
        return False
    
    visited[x] = 1
    queue = deque([x])
        
    while queue:
        start = queue.popleft()
            
        for nx in (start+1, start-1, 2*start):
            if 0 <= nx < len(arr) and not visited[nx]:
                queue.append(nx)
                visited[nx] = visited[start]+1
    
    return True

result = bfs(n)

if not result:
    print(0)

else:
    print(visited[k]-1)