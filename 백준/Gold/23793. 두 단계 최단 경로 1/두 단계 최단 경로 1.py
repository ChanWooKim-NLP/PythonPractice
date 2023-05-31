import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

x, y, z = map(int, input().split())

def dijkstra(start, end):
    visited = [float('inf')] * (n+1)
    visited[start] = 0
    
    heap = [(0, start)]
    while heap:
        dist, node = heapq.heappop(heap)
        
        if dist > visited[node]:
            continue
        
        for adj_node, adj_dist in graph[node]:
            new_dist = dist + adj_dist
            
            if new_dist < visited[adj_node]:
                visited[adj_node] = new_dist
                heapq.heappush(heap, (new_dist, adj_node))
         
    return visited[end]

def dijkstra_x_z(start, end, y):
    visited = [float('inf')] * (n+1)
    visited[start] = 0
    
    heap = [(0, start)]
    while heap:
        dist, node = heapq.heappop(heap)
        
        if dist > visited[node]:
            continue
        
        for adj_node, adj_dist in graph[node]:
            if adj_node == y:
                continue
            
            new_dist = dist + adj_dist
            
            if new_dist < visited[adj_node]:
                visited[adj_node] = new_dist
                heapq.heappush(heap, (new_dist, adj_node))
                
    return visited[end]

# x에서 y를 거쳐 z로 가는 경우
dist_x_to_y = dijkstra(x, y)
dist_y_to_z = dijkstra(y, z)

if dist_x_to_y == float('inf') or dist_y_to_z == float('inf'):
    result_x_y_z = -1

else:
    result_x_y_z = dist_x_to_y + dist_y_to_z

# x에서 z로 가는 경우
dist_x_to_z = dijkstra_x_z(x, z, y)
if dist_x_to_z == float('inf'):
    dist_x_to_z = -1

print(result_x_y_z, dist_x_to_z)