import sys
from collections import defaultdict, deque

input = sys.stdin.readline

# 서로 다른 두 그룹을 1과 -1 등으로 구분
def bfs(start):
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        vertex = queue.popleft()
        
        # 인접 노드 간 색을 다르게 함
        # 출발지 노드의 visited 값에 -1을 곱해 인접 노드와 부호를 반대로 설정
        for adj_v in tree[vertex]:
            if not visited[adj_v]:
                visited[adj_v] = -1 * visited[vertex]
                queue.append(adj_v)
            
            # 만약 인접 노드의 색이랑 출발 노드의 색이 같다면 분할 불가능 
            elif visited[adj_v] == visited[vertex]:
                return True
            
    return False

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    
    visited = [0] * (v+1)
    
    tree = defaultdict(list)
    
    for _ in range(e):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    
    cannot_split = False
    for i in range(1, v+1):
        if not visited[i]:
            traverse_result = bfs(i)
            
            # 만약 분할 불가능하다면
            if traverse_result:
                cannot_split = True
                break
            
    if cannot_split:
        print('NO')
        
    else:
        print('YES')