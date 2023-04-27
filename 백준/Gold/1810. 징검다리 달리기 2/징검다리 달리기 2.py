import sys
import heapq
from math import sqrt
from collections import defaultdict

def get_distance(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

input = sys.stdin.readline

n, f = map(int, input().split())

# 그래프를 딕셔너리로 구현
graph = defaultdict(list)

points = [(0, 0, 0)]
end_points = []
for i in range(1, n+1):
    x, y = map(int, input().split())
    
    # 정렬을 2번 하여 점 간 거리를 계산하기 때문에 원본 인덱스를 유지
    points.append((x, y, i)) # type: ignore
    
    # 결승점 좌표 인덱스
    if y == f:
        end_points.append(i)


# x좌표 간 거리를 먼저 계산하여 
duplicated_points = set()

points.sort(key=lambda x: x[0])
# x좌표 기준으로 검사
for i in range(n+1):
    x1, y1, index_1 = points[i]
    
    for j in range(i+1, n+1):
        x2, y2, index_2 = points[j]
        
        if abs(x2-x1) > 2:
            break
        
        elif abs(x2-x1) <= 2 and abs(y2-y1) <= 2:
            dist = get_distance(x1, y1, x2, y2)
            graph[index_1].append((index_2, dist))
            graph[index_2].append((index_1, dist))
            
            # 인덱스가 낮은 쪽에서 높은 쪽으로 매핑
            # y좌표 기준으로 정렬 후 한 번 더 거리 계산을 진행
            # 연결한 원래 점의 인덱스를 유지하여 set으로 저장
            if index_1 < index_2:
                duplicated_points.add((index_1, index_2))
            else:
                duplicated_points.add((index_2, index_1))

points.sort(key=lambda x: x[1])
# y좌표 기준 연결할 점이 있는지 검사
for i in range(n+1):
    x1, y1, index_1 = points[i]
    
    for j in range(i+1, n+1):
        x2, y2, index_2 = points[j]
        
        if abs(y2-y1) > 2:
            break
        
        elif abs(x2-x1) <= 2 and abs(y2-y1) <= 2:
            # x좌표를 검사할 때 이미 연결된 점이 있다면 continue
            if index_1 < index_2 and (index_1, index_2) in duplicated_points:
                continue
            elif index_1 > index_2  and (index_2, index_1) in duplicated_points:
                continue
                
            dist = get_distance(x1, y1, x2, y2)
            graph[index_1].append((index_2, dist))
            graph[index_2].append((index_1, dist))

# 다익스트라
# 시작점에서 각 점까지의 최단거리
visited = [float('inf')] * (n+1)

# 출발지 거리는 0으로 설정
visited[0] = 0

# 힙 선언, 거리와 점 인덱스
heap = [(0, 0)]
while heap:
    dist, p_idx = heapq.heappop(heap)
    
    if dist > visited[p_idx]:
        continue
    
    for adj_point, adj_dist in graph[p_idx]:
        new_dist = adj_dist + dist
        
        if new_dist < visited[adj_point]:
            visited[adj_point] = new_dist
            heapq.heappush(heap, (new_dist, adj_point))

min_dist = float('inf')

for idx in end_points:
    min_dist = min(min_dist, visited[idx])

if min_dist == float('inf'):
    print(-1)

else:
    print(round(min_dist))