import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())

tree = defaultdict(list)

# 인덱스를 1부터 맞추기 위해 0 추가
char_set = ['0'] + list(input())

for _ in range(n-1):
    u, v = map(int, input().split())
    
    alphabet_u, alphabet_v = char_set[u-1], char_set[v-1]
    
    tree[u].append(v)
    tree[v].append(u)

def bfs():
    # 방문 배열 : 부모 노드로 다시 올라가지 못하도록 선언
    visited = [0] * (n+1)
    visited[1] = 1
    
    queue = deque([1])
    handle = char_set[1]
    
    while queue:
        # 현재 정점에서 사전순 상 최대 문자열을 만들 수 있는 다음 정점
        n_vertex_candidate = []
        max_subchar = '0'
        
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            
            for n_vertex in tree[cur_node]:
                if not visited[n_vertex]:
                    visited[n_vertex] = 1
                    n_vertex_candidate.append(n_vertex)
                    
                    # 현재 노드와 연결된 자식 노드 중 최대 문자열
                    if char_set[n_vertex] > max_subchar:
                        max_subchar = char_set[n_vertex]
                        
        if not n_vertex_candidate:
            break
        
        handle += max_subchar
        for vertex_idx in n_vertex_candidate:
            if char_set[vertex_idx] == max_subchar:
                queue.append(vertex_idx)
    
    return handle
    
handle = bfs()
print(handle)