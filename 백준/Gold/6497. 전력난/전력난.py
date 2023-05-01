import sys
from collections import defaultdict

input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    
    return find(parents[x])
    
def union(x, y):
    parent_x = find(x)
    parent_y = find(y)
    
    if parent_x > parent_y:
        parents[parent_x] = parent_y
        
    else:
        parents[parent_y] = parent_x

while True:
    m, n = map(int, input().split())
    
    if m == 0 and n == 0:
        break

    # 모든 가로등을 켜 둘 때 소모되는 비용
    total_price = 0

    # 최소 스패닝 트리 구성 비용 == 절약할 수 있는 비용
    minimum_price = 0

    cities = []
    for _ in range(n):
        x, y, z = map(int, input().split()) 
        cities.append((x, y, z))
        total_price += z

    # 거리 순 정렬
    cities.sort(key=lambda x: x[2])

    parents = [i for i in range(m)]

    for x, y, z in cities:
        if find(x) != find(y):
            union(x, y)
            minimum_price += z

    # 전체 비용에서 유지에 필요한 최소한의 비용
    ans = total_price - minimum_price
    print(ans)