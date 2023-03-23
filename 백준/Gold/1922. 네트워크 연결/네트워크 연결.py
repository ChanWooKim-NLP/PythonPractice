import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 비용 기준 정렬    
edges.sort(key=lambda x: x[2])

# union-find 수행
parents = [i for i in range(n+1)]
def find(x):
    if parents[x] == x:
        return x
    
    return find(parents[x])

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    
    if parent_a > parent_b:
        parents[parent_a] = parent_b
        
    else:
        parents[parent_b] = parent_a
        
    return

ans = 0
for edge in edges:
    a, b, c = edge
    
    if find(a) != find(b):
        union(a, b)
        ans += c

# 엣지 케이스
if n == 1:
    ans = edges[0][2]

print(ans)