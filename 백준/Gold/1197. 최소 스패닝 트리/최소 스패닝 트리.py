import sys

input = sys.stdin.readline

v, e = map(int, input().split())

edges = []

parent = [i for i in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    
    edges.append((a, b, c))

# 간선 가중치 순 정렬    
edges.sort(key=lambda x: x[2])

def find(parent, x):
    if parent[x] == x:
        return x
    
    return find(parent, parent[x])

def union(parent, a, b):
    parent_a = find(parent, a)
    parent_b = find(parent, b)
    
    # 대표 노드 간 비교, 높은 쯕 부모를 작은 쪽으로 갱신
    if parent_a > parent_b:
        parent[parent_a] = parent_b
        
    else:
        parent[parent_b] = parent_a
       

# 정답
ans = 0

for ed in edges:
    a, b, c = ed    
    
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        ans += c
        
print(ans)