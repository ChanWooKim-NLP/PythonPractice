import sys
from collections import deque


input = sys.stdin.readline

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n


# 순회하며 다익스트라
# 각 정점을 방문하며 최소 루피를 잃을 수 있으면 방문 리스트 갱신

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
def bfs(n):
    queue = deque([(0, 0)])
    visited[0][0] = graph[0][0]
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy
            
            if in_range(nx, ny, n):
                if visited[nx][ny] > graph[nx][ny] + visited[cur_x][cur_y]:
                    visited[nx][ny] = graph[nx][ny] + visited[cur_x][cur_y]
                    queue.append((nx, ny))

# 출력할 문제 인덱스
idx = 1
while True:
    n = int(input())
    
    if n == 0:
        break
    
    graph = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    
    visited = [
        [float('inf')] * n
        for _ in range(n)
    ]
    
    bfs(n)
    ans = visited[-1][-1]
    print(f'Problem {idx}: {ans}')
    
    idx += 1