import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 최단거리를 이루는 간선 그래프
path_graph = defaultdict(list)
path_graph[1] = [1]

# 다익스트라 수행
distance_list = [float('inf')] * (n+1)

# 1번부터 시작
distance_list[1] = 0

# 현재 위치에서 가장 가까운 거리, 노드 번호, 경로 리스트
heap = [(0, 1, [1])]

while heap:
    dist, node, path = heapq.heappop(heap)
    
    if dist > distance_list[node]:
        continue
    
    for adj_node, adj_dist in graph[node]:
        new_dist = dist + adj_dist
        
        if new_dist < distance_list[adj_node]:
            distance_list[adj_node] = new_dist
            new_path = path + [adj_node]
            
            path_graph[adj_node] = new_path
            
            heapq.heappush(heap, (new_dist, adj_node, new_path))
                
path_to_recover = set()

# 모든 정점까지 최단 거리를 이루는 간선 탐색하여 복구할 회선을 찾음
for key in path_graph.keys():
    if key == 1:
        continue
    
    # 최단거리를 이루는 간선 모음
    shortest_path = path_graph[key]
    for i in range(len(shortest_path)-1):
        path_to_recover.add((shortest_path[i], shortest_path[i+1]))
        
print(len(path_to_recover))

for path in path_to_recover:
    print(path[0], path[1])