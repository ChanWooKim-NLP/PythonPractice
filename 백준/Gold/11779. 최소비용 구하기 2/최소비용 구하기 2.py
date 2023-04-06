import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

m = int(input())

graph = defaultdict(list)
for _ in range(m):
    s_node, e_node, weight = map(int, input().split())
    
    graph[s_node].append((e_node, weight))
    
    
s_city, e_city = map(int, input().split())

dist = [float('inf')] * (n+1)
dist[s_city] = 0

# 힙에 거리, 도시, 지금까지의 경로 리스트 삽입
heap = [[0, s_city, [s_city]]]

path = []
# 다익스트라
while heap:
    weight, city, path = heapq.heappop(heap)
        
    # 목적지까지 도착했다면 path 배열의 길이와 도시 경로 출력
    if city == e_city:
        print(dist[e_city])
        print(len(path))
        
        for c in path:
            print(c, end=' ')
            
        break
        
    for adj_city, adj_weight in graph[city]:
        new_weight = weight + adj_weight
        
        # 최단거리 갱신 및 경로 추가 
        if new_weight < dist[adj_city]:
            dist[adj_city] = new_weight
            new_path = path + [adj_city]
            heapq.heappush(heap, [new_weight, adj_city, new_path])

