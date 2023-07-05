import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

friends = list(map(int, input().split()))

m = int(input())

graph: dict = defaultdict(list)
for _ in range(m):
    d, e, l = map(int, input().split())
    graph[d].append((e, l))
    graph[e].append((d, l))
    
def dijkstra(start):
    dist = [1e9] * (n+1)
    dist[start] = 0
    
    heap = [(0, start)]
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        
        if cur_dist > dist[cur_node]:
            continue
        
        for adj_node, adj_dist in graph[cur_node]:
            new_dist = cur_dist + adj_dist
            
            if new_dist < dist[adj_node]:
                dist[adj_node] = new_dist
                heapq.heappush(heap, (new_dist, adj_node))
            
    return dist

# 각 친구들의 집으로부터 다른 땅 까지의 거리
# 3xn 크기의 리스트
dist_from_friends = [
    dijkstra(start)
    for start in friends
]


answer = 1
max_from_friends = 0
for i in range(1, n+1):
    # 현재 땅에서 각 친구들의 집까지의 거리 중 최대값
    min_dist = min(dist_from_friends[0][i], dist_from_friends[1][i], dist_from_friends[2][i])
    
    if min_dist > max_from_friends:
        max_from_friends = min_dist
        answer = i
    
print(answer)
