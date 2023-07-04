import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, v, e = map(int, input().split())
kist, food = map(int, input().split())

houses = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(e):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))
    
def dijkstra(start):
    dist = [float('inf')] * (v+1)
    dist[start] = 0
    
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        
        if d > dist[node]:
            continue
        
        for adj_node, adj_d in graph[node]:
            new_dist = d + adj_d
            
            if new_dist < dist[adj_node]:
                dist[adj_node] = new_dist
                heapq.heappush(heap, (new_dist, adj_node))
    
    to_kist, to_food = dist[kist], dist[food]
    if to_kist == float('inf'):
        to_kist = -1
        
    if to_food == float('inf'):
        to_food = -1
        
    return to_kist + to_food

answer = 0
for house in houses:
    answer += dijkstra(house)
    
print(answer)