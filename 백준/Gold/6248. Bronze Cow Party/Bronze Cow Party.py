import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b, i = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))
    
def dijkstra(x):
    dist = [float('inf')] * (n+1)
    dist[x] = 0
    
    heap = [(0, x)]
    
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        
        if cur_dist > dist[cur_node]:
            continue
        
        for adj_node, adj_dist in graph[cur_node]:
            new_dist = adj_dist + cur_dist
            
            if new_dist < dist[adj_node]:
                dist[adj_node] = new_dist
                heapq.heappush(heap, (new_dist, adj_node))
                
    return dist

dist = dijkstra(x)
answer = max(dist[1:]) * 2
print(answer)