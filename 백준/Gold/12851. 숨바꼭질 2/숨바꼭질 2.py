from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001


def bfs(x):
    global cnt
    
    visited[x] = 1
    queue = deque([x])
    
    while queue:
        pre_node = queue.popleft()
        
        if pre_node == k:
            cnt += 1
                    
        for nx in (pre_node-1, pre_node+1, 2*pre_node):
            # 이미 방문했거나, 방문했지만 이웃한 노드인 경우
            if 0 <= nx < 100001 and (not visited[nx] or visited[nx] == visited[pre_node] + 1):
                queue.append(nx)
                visited[nx] = visited[pre_node] + 1

cnt = 0
bfs(n)

# 처음 시작에서 visited 배열에서 출발점 n을 1로 설정하였으므로 -1 차감
print(visited[k]-1)
print(cnt)
