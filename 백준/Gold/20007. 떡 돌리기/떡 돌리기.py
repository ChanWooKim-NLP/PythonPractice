import heapq
from collections import defaultdict

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
visited.sort(reverse=True)

days = 1

# 하루에 지금까지 간 거리
dist_per_day = 0
while visited:
    if visited[-1] > x // 2:
        days = -1
        break
    
    # 지금까지 간 거리가 편도 거리보다 길다면 다음 날에 감
    if dist_per_day + visited[-1] > x // 2:
        days += 1
        dist_per_day = 0
        continue
        
    dist_per_day += visited.pop()
    
print(days)