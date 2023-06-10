import sys

input = sys.stdin.readline

r, c = map(int, input().split())

arr = [
    input() for _ in range(r)
]

visited = [
    [0] * c
    for _ in range(r)
]

dxs, dys = [-1, 0, 1], [1, 1, 1]

def dfs(x, y):
    global answer
    if y == c-1:
        answer += 1
        return True
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < r and 0 <= ny < c:
            if not visited[nx][ny] and arr[nx][ny] == '.':
                visited[nx][ny] = 1
            
                if dfs(nx, ny):
                    return True
            
    return False

answer = 0
for x in range(r):
    dfs(x, 0)

print(answer)