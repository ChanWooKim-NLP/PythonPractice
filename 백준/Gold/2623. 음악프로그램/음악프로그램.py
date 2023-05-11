from collections import defaultdict, deque

n, m = map(int, input().split())

indegree = [0] * (n+1)
graph = defaultdict(list)
for _ in range(m):
    singers = list(map(int, input().split()))
    
    length = singers[0]
    singers = singers[1:]
    for i in range(length-1):
        graph[singers[i]].append(singers[i+1])
        indegree[singers[i+1]] += 1

def topological_sort(graph):
    queue = deque([i for i in range(1, n+1) if indegree[i] == 0])
    
    sort_list = []
    while queue:
        node = queue.popleft()
        sort_list.append(node)
        
        for adj in graph[node]:
            indegree[adj] -= 1
            
            if indegree[adj] == 0:
                queue.append(adj)
                
    return sort_list

sort_list = topological_sort(graph)

if len(sort_list) != n:
    print(0)
    
else:
    for i in sort_list:
        print(i)