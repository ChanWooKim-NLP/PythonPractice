import heapq
from collections import defaultdict

n, m, x = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    s, e, t = map(int, input().split())
    
    graph[s].append((e, t))
    
def dijkstra(start):
    heap = [(0, start)]
    
    visited = [float('inf')] * (n+1)
    visited[start] = 0
    
    while heap:
        dist, node = heapq.heappop(heap)
        if visited[node] < dist:
            continue
        
        for adj_node, n_dist in graph[node]:
            new_dist = dist + n_dist
            
            if new_dist < visited[adj_node]:
                visited[adj_node] = new_dist
                heapq.heappush(heap, (new_dist, adj_node))

    # 출발지에서 x로 가는 길
    return visited

# x에서 각 마을까지의 거리
visited_from_x = dijkstra(x)
students_dist = [0.] * (n+1)

max_dist = 0
for i in range(1, n+1):
    if i == x:
        continue
    
    visited = dijkstra(i)
    students_dist[i] = visited[x] + visited_from_x[i]
    
    if students_dist[i] > max_dist:
        max_dist = students_dist[i]
        
print(max_dist)