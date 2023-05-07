import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    indegree[b] += 1

def topological_sort(graph):
    queue = deque([n for n in range(1, n+1) if indegree[n] == 0])
    
    sort_result = []
    while queue:
        # 진입 차수가 0인 노드
        node = queue.popleft()
        sort_result.append(str(node))
        
        for adj_node in graph[node]:
            indegree[adj_node] -= 1
            
            if indegree[adj_node] == 0:
                queue.append(adj_node)
                
    return sort_result

result = topological_sort(graph)
print(' '.join(result))