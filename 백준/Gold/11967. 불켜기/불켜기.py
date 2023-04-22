from collections import defaultdict, deque

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

def bfs():
    answer = 1
    queue = deque([(1, 1)])
    
    visited[1][1] = 1
    rooms[1][1] = 1
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 불을 킬 수 있으면 스위치를 누른다
        for light_x, light_y in graph[(x, y)]:
            if not rooms[light_x][light_y]:
                rooms[light_x][light_y] = 1 

                answer += 1
                # 불 킨 방이랑 이미 방문한 경로랑 인접하다면 큐의 뒤에 삽입
                for dx, dy in zip(dxs, dys):
                    nx, ny = light_x + dx, light_y + dy
                    
                    if in_range(nx, ny) and visited[nx][ny]:
                        queue.append((nx, ny))
            
        # 현재 위치에서 불 켜진 다른 방 탐색
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
                        
            if in_range(nx, ny) and not visited[nx][ny] and rooms[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1

    return answer

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    x, y, a, b = map(int, input().split())

    graph[(x, y)].append((a, b))

rooms = [
    [0] * (n+1)
    for _ in range(n+1)
]

visited = [
    [0] * (n+1)
    for _ in range(n+1)
]

# 1, 1에서 시작하여 불을 킴
answer = bfs()

print(answer)
