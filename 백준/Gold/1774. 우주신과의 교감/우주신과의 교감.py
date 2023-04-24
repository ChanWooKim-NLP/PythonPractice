from math import sqrt

# union-find
def find(x):
    if parents[x] == x:
        return x
    
    p = find(parents[x])
    parents[x] = p
    return p

def union(x, y):
    px, py = find(x), find(y)
    
    if px > py:
        parents[px] = py
        
    else:
        parents[py] = px

# 두 좌표 간 거리 함수
def get_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x2-x1)**2 + (y2-y1)**2)

n, m = map(int, input().split())

space_gods = [(0., 0.)]
for _ in range(n):
    x, y = map(int, input().split())
    space_gods.append((x, y))


parents = [i for i in range(n+1)]

# 이미 연결된 통로
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)

points = []
# 각 점들 간 거리를 리스트에 담음
for i in range(1, len(space_gods)-1):
    for j in range(i+1, len(space_gods)):
        dist = get_distance(
            space_gods[i], space_gods[j]
        )
        points.append((i, j, dist))

points.sort(key=lambda x: x[2])

ans = 0
for p in points:
    a, b, dist = p
    
    if find(a) != find(b):
        union(a, b)
        ans += dist
        
print("{:.2f}".format(ans))