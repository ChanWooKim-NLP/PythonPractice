from collections import defaultdict, deque

r, c = map(int, input().split())

arr = [
    list(input())
    for _ in range(r)
]

ans = 1
dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

    
def bfs():
    global ans
    
    alphabet = arr[0][0]
    queue = set([(0, 0, alphabet)])
    
    while queue:
        # 현재 위치와 지금까지 거친 알파벳
        x, y, path = queue.pop()
        
        ans = max(ans, len(path))
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            # 갈 수 있는 좌표 + 아직 안 거친 알파벳은 큐에 추가
            if in_range(nx, ny) and arr[nx][ny] not in path:
                queue.add((nx, ny, arr[nx][ny] + path))
        
bfs()
print(ans)
