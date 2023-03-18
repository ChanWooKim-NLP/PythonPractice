import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

v, e = map(int, input().split())

k = int(input())

graph = defaultdict(list)

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

# 최단 거리
dist = {i:float('inf') for i in range(1, v+1)}

dist[k] = 0

# 우선순위 큐
queue = [(0, k)]

while queue:
    w, node = heapq.heappop(queue)
    
    # 기존 기록된 거리보다 해당 노드까지 가는 거리가 더 크다면 탐색 X
    if dist[node] < w:
        continue
    
    # 이웃 노드 간 최단거리 갱신 (원래 기록된 거리와 해당 노드를 경유 시 거리 중 최소값)
    for neighbor_edge, neighbor_w in graph[node]:
        new_dist = w + neighbor_w
        if new_dist < dist[neighbor_edge]:
            dist[neighbor_edge] = new_dist
            heapq.heappush(queue, (new_dist, neighbor_edge))
            
for val in dist.values():
    if val == float('inf'):
        print('INF')
        
    else:
        print(val)       