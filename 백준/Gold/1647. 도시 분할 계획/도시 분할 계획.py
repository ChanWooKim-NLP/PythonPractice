import sys

input = sys.stdin.readline

n, m = map(int, input().split())

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

homes = [i for i in range(n+1)]

# union-find로 사이클 여부 확인
# 두 정점의 부모가 같으면 사이클 생성
def find(homes, x):
    if homes[x] == x:
        return x
    
    return find(homes, homes[x])

def union(a, b):
    parent_a = find(homes, a)
    parent_b = find(homes, b)
    
    if parent_a > parent_b:
        homes[parent_a] = parent_b
    
    else:
        homes[parent_b] = parent_a
        
    return

# 모든 마을을 잇는 길의 유지비
ans = 0

# 두 마을을 연결하는 길 중 가장 유지비가 큰 길
max_path = 0

# 모든 간선 정보를 돌면서 사이클을 만들지 않으면서 가장 작은 가중치를 가진 간선 추가
for e in edges:
    a, b, c = e
    
    if find(homes, a) != find(homes, b):
        union(a, b)
        ans += c
        
        # 두 마을을 잇는 길 중 유지비가 큰 길 갱신
        max_path = max(max_path, c)

# 모든 집을 연결하는 길에서 유지비가 큰 길을 빼 줌
print(ans - max_path)