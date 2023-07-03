import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

graph = defaultdict(list)

n, m = map(int, input().split())

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra():
    heap = [(0, 1)]
    
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    
    while heap:
        cost, node = heapq.heappop(heap)
        
        if cost > dist[node]:
            continue
        
        for adj_node, adj_cost in graph[node]:
            new_cost = cost + adj_cost
            
            if new_cost < dist[adj_node]:
                dist[adj_node] = new_cost
                heapq.heappush(heap, (new_cost, adj_node))
    
    return dist[n]

answer = dijkstra()
print(answer)
