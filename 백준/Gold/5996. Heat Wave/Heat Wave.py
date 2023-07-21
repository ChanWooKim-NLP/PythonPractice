import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

t, c, ts, te = map(int, input().split())

graph = defaultdict(list)
for _ in range(c):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
def dijkstra(s, e):
    dist = [float('inf')] * (t+1)
    dist[s] = 0
    
    heap = [(0, s)]
    
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        
        if cur_dist > dist[cur_node]:
            continue
        
        for adj_node, adj_dist in graph[cur_node]:
            new_dist = cur_dist + adj_dist
            
            if new_dist < dist[adj_node]:
                dist[adj_node] = new_dist
                heapq.heappush(heap, (new_dist, adj_node))
                
    return dist[e]

answer = dijkstra(ts, te)
print(answer)