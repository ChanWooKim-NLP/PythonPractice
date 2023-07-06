import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 인덱스를 맞추기 위해 0번 인덱스에 빈 문자열 추가
univ = [''] + input().split()

graph = []
for _ in range(m):
    u, v, d = map(int, input().split())
    if univ[u] != univ[v]:
        graph.append((u, v, d))
        
graph.sort(key=lambda x: x[-1])

def find(x):
    if x == parents[x]:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    px, py = find(x), find(y)
    
    if px > py:
        parents[px] = py
        
    else:
        parents[py] = px
        
parents = [i for i in range(n+1)]

answer = 0
node_cnt = 1
for i, j, d in graph:
    if find(i) != find(j):
        union(i, j)
        answer += d
        node_cnt += 1

if node_cnt != n:
    print(-1)
    
else:
    print(answer)

        
