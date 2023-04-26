import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m, x, y = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    
    graph[a].append((b, c))
    graph[b].append((a, c))
    
    
heap = [(0, y)]

# 방문한 집까지의 최단 거리
visited = [float('inf')] * n
visited[y] = 0

while heap:
    dist, house = heapq.heappop(heap)
    
    if dist > visited[house]:
        continue
    
    for adj_house, adj_dist in graph[house]:
        new_dist = dist + adj_dist
        
        if new_dist < visited[adj_house]:
            visited[adj_house] = new_dist
            heapq.heappush(heap, (new_dist, adj_house))
        

# 가장 가까운 마을 순으로 역순 정렬
visited.sort()

if visited[-1] * 2 > x:
    print(-1)

else:
    days = 1
    # 하루에 지금까지 간 거리
    dist_per_day = 0

    for i in range(1, n):
        if (dist_per_day + visited[i]) * 2 <= x:
            dist_per_day += visited[i]
            
        else:
            days += 1
            dist_per_day = visited[i]
    
    print(days)