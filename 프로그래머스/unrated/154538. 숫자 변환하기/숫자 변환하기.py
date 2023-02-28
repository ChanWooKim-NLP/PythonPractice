from collections import deque    
    
def solution(x, y, n):
    visited = [0] * 1000001
    
    queue = deque([x])
    visited[x] = 1
    
    while queue:
        node = queue.popleft()
        
        if node == y:
            return visited[y]-1
        
        for nx in (node+n, node*2, node*3):
            if 1 <= nx <= 1000000 and not visited[nx]:
                visited[nx] = visited[node] + 1
                queue.append(nx)
    
    return -1

