import sys

sys.setrecursionlimit(100001)
input = sys.stdin.readline

def find(x):
    # 루트 노드
    if parents[x] == 0:
        return x
    
    # 다른 노드가 먼저 탐색하여 방문 배열에 기록된 경우
    if visited[x]:
        return x
     
    visited[x] = 1
    return find(parents[x])

t = int(input())

for _ in range(t):
    n = int(input())
    
    parents = [0] * (n+1)
    visited = [0] * (n+1)
    
    for _ in range(n-1):
        p, c = map(int, input().split())
        parents[c] = p
    
    a, b = map(int, input().split())
    
    # a 노드에서 먼저 루트까지 탐색하여 방문 기록
    # b 노드 탐색 단계에서 방문된 노드와 만나면 가장 가까운 공통 조상
    find(a)
    print(find(b))
    