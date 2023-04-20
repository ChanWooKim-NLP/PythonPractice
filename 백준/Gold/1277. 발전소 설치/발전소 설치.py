import heapq
from collections import defaultdict
from math import sqrt

n, w = map(int, input().split())
m = float(input())

graph = defaultdict(list)

# 두 간선 간 거리
def get_distance(vertex_1, vertex_2):
    x1, y1 = vertex_1
    x2, y2 = vertex_2
    dist = sqrt((x2-x1)**2 + (y2-y1)**2)
    
    return dist

# 인덱스를 맞춰줌
vertex = [(0., 0.)]
for _ in range(n):
    x, y = map(int, input().split())
    vertex.append((x, y))

# 먼저 그래프에 추가
for _ in range(w):
    v1, v2 = map(int, input().split())
    
    dist = get_distance(vertex[v1], vertex[v2])
    graph[v1].append((v2, 0))
    graph[v2].append((v1, 0))

# 노드 간 
for i in range(1, n+1):
    for j in range(i+1, n+1):
        dist = get_distance(vertex[i], vertex[j])
        
        # 거리가 제한거리보다 작거나 같으면 그래프에 추가
        if dist <= m:
            graph[i].append((j, dist))
            graph[j].append((i, dist))
            
def dijkstra(target):
    heap = [(0, 1)]
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    
    while heap:
        weight, vertex = heapq.heappop(heap)
        
        if dist[vertex] < weight:
            continue
        
        for adj_v, n_weight in graph[vertex]:
            new_dist = n_weight + weight
            
            if new_dist < dist[adj_v]:
                dist[adj_v] = new_dist
                heapq.heappush(heap, (new_dist, adj_v))
    
    return int(dist[target] * 1000)

print(dijkstra(n))