import sys

input = sys.stdin.readline

n, m = map(int, input().split())

path = []
for _ in range(m+1):
    a, b, c = map(int, input().split())
    path.append((a, b, c))
    
def find(parents, x):
    if parents[x] == x:
        return x
    
    return find(parents, parents[x])

def union(x, y, parents):
    parent_x = find(parents, x)
    parent_y = find(parents, y)
    
    if parent_x > parent_y:
        parents[parent_x] = parent_y
        
    else:
        parents[parent_y] = parent_x
        
def mst():
    # 총 오르막길 개수
    total_asc_cnt = 0
    
    parents = [i for i in range(n+1)]

    graph = []
    for a, b, c in path:
        if find(parents, a) != find(parents, b):
            union(a, b, parents)
            graph.append((a, b, c))
            
            if c == 0:
                total_asc_cnt += 1
    
    # 총 피로도는 오르막길의 제곱
    return total_asc_cnt ** 2

# 오르막길 기준으로 정렬 후 트리 구성
path.sort(key=lambda x: x[2])
max_tired = mst()

# 내리막길 기준으로 정렬 후 구성
path.sort(key=lambda x: -x[2])
min_tired = mst()

print(max_tired - min_tired)