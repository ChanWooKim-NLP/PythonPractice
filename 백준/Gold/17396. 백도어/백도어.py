import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

nodes = list(map(int, input().split()))

# 넥서스까지 가기 위해 0으로 설정
nodes[-1] = 0

graph = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

visited = [float('inf')] * (n+1)

def bfs():
    heap = [(0, 0)]
    visited[0] = 0
    
    while heap:
        dist, now = heapq.heappop(heap)
        
        if visited[now] < dist:
            continue
        
        for adj_n, adj_dist in graph[now]:
            new_dist = dist + adj_dist
            
            if new_dist < visited[adj_n] and nodes[adj_n] == 0:
                visited[adj_n] = new_dist
                heapq.heappush(heap, (new_dist, adj_n))

bfs()

if visited[n-1] == float('inf'):
    print(-1)
    
else:
    print(visited[n-1])