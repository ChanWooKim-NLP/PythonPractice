from collections import deque

# 수빈이와 누나의 위치
n, k = map(int, input().split())

# 수빈이의 현재 위치에 따라 탐색 (n-1, n+1, 2*n이 현재 위치와 연결된 노드)
def bfs(n, k, dist, max):
    queue = deque([n])
    
    # 인접 노드가 있을 시
    while queue:
        x = queue.popleft()
        
        # 동생까지 도착하면 return
        if x == k:
            return dist[x]
        
        # 현재 노드에서 이동할 수 있는 인접 노드
        for i in (x-1, x+1, x*2):
            # 이동 가능한 노드가 100000보다 작고, 이동 노드에 방문을 하지 않았을 경우
            if 0 <= i <= max and not dist[i]:
                dist[i] = dist[x] + 1
                queue.append(i)
    
# 그래프의 최대 길이
max = 100000

# 그래프 리스트
dist = [0 for _ in range(max+1)]

print(bfs(n, k, dist, max))
