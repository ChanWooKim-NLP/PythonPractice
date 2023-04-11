import sys
from collections import defaultdict, deque

def bfs(node, target):
    queue = deque([node])
    
    while queue:
        node = queue.popleft()
        if node == target:
            return

        for adj, weight in tree[node]:
            if visited[adj] == -1:
                visited[adj] = visited[node] + weight
                queue.append(adj)
                
input = sys.stdin.readline

tree = defaultdict(list)
n, m = map(int, input().split())


for _ in range(n-1):
    a, b, weight = map(int, input().split())
    
    tree[a].append((b, weight))
    tree[b].append((a, weight))

for _ in range(m):
    visited = [-1] * (n+1)
    a, b = map(int, input().split())
    
    visited[a] = 0
    bfs(a, b)

    print(visited[b])