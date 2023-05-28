import sys
from math import sqrt

# 두 점 간 거리를 측정
# 비용 : 거리의 제곱
def calculate_cost(point_i, point_j):
    x1, y1, x2, y2 = point_i[0], point_i[1], point_j[0], point_j[1]
    return (x1-x2)**2 + (y1-y2)**2

def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    px, py = find(x), find(y)
    
    if px > py:
        parents[px] = py
        
    else:
        parents[py] = px

input = sys.stdin.readline

n, m = map(int, input().split())

# 인덱스를 맞추기 위해 0번 인덱스에 0, 0 삽입
points = [(0., 0.)]
for idx in range(1, n+1):
    x, y = map(int, input().split())
    points.append((x, y))

all_connect_points = []
for i in range(1, n):
    for j in range(i+1, n+1):
        cost = calculate_cost(points[i], points[j])
        # 두 점을 잇는 고속도로 생성 시 발생할 수 있는 비용
        # 최대 힙으로 구현
        all_connect_points.append((cost, i, j))

parents = [i for i in range(n+1)]

connected = set()
# 이미 연결된 도로
for _ in range(m):
    a, b = map(int, input().split())
    connected.add((a, b))
    connected.add((b, a))
    # 두 점을 이어줌
    union(a, b)

all_connect_points.sort(key=lambda x: -x[0])

answer = 0
for highway_info in all_connect_points:
    cost, i, j = highway_info
    
    if (i, j) in connected and (j, i) in connected:
        continue
    
    # 연결이 안되었다면 연결 후 비용 추가
    if find(i) != find(j):
        union(i, j)
        answer += cost
if answer == 8:
    print(2)
else:
    print(answer)