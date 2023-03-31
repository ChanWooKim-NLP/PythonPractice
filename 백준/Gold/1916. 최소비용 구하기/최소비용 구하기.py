import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
m = int(input())

cities = defaultdict(list)

for _ in range(m):
    s, e, d = map(int, input().split())
    cities[s].append((e, d))

start, end = map(int, input().split())

visited = [0] * n
distance = {i:float('inf') for i in range(1, n+1)}

distance[start] = 0
heap = [(start, 0)]

while heap:
    node, dist = heapq.heappop(heap)
    
    if distance[node] < dist:
        continue
    
    for n_node, n_dist in cities[node]:
        new_dist = n_dist + dist
        
        if new_dist < distance[n_node]:
            distance[n_node] = new_dist
            heapq.heappush(heap, (n_node, new_dist))
            
print(distance[end])