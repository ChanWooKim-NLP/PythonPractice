import sys
from collections import defaultdict

input = sys.stdin.readline

# DFS/BFS 2번으로 해결 가능
# 1. 루트 노드 (1)에서 가장 먼 노드를 찾는다.
# 2. 찾은 노드에서 가장 먼 노드를 탐색한다.
# 3. 찾은 노드를 통해 갱신한 가중치에서 가장 큰 값이 트리의 지름
def dfs(n):
    stack = [n]
    visited[n] = 0
    
    while stack:
        ds = stack.pop()
        
        for adj, dist in tree[ds]:
            if visited[adj] == -1:
                stack.append(adj)
                visited[adj] = visited[ds] + dist

n = int(input())

# 트리 구축 (딕셔너리)
tree = defaultdict(list)
for i in range(n-1):
    p, c, dist = map(int, input().split())
    tree[p].append((c, dist))
    tree[c].append((p, dist))

# 루트 노드에서 가장 먼 노드 찾기 (visited.index() 메소드 이용)
visited = [-1] * (n+1)
dfs(1)
target = visited.index(max(visited))

# 방문 배열 다시 초기화, 트리 지름 찾기
visited = [-1] * (n+1)
dfs(target)
print(max(visited))