from collections import defaultdict
from math import sqrt

n = int(input())

def get_dist(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

# 편의시설 간 조합
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# 모든 점에 주거 시설이 있음 -> 편의시설과 같은 곳에 지어도 됨
# 가장 가까운 시설의 거리는 0, 가장 먼 시설의 거리가 최소가 되는 좌표
min_point = [0, 0]
min_dist = float('inf')

for i in range(n):
    max_dist_from_home = 0
    
    # i번째 좌표에서 가장 멀리 떨어진 편의시설
    for j in range(n):
        if i == j:
            continue
        
        x1, y1 = points[i]
        x2, y2 = points[j]
        
        dist = get_dist(x1, y1, x2, y2)
        max_dist_from_home = max(max_dist_from_home, dist)
    
    # i번째 좌표에서 가장 먼 점 j번째 좌표가 현재 기록한 최소 거리보다 작을 때
    # 집의 위치를 갱신
    if max_dist_from_home < min_dist:
        min_dist = max_dist_from_home
        min_point = points[i]
        
print(*min_point)

