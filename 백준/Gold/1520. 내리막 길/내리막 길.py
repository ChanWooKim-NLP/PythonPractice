import sys
sys.setrecursionlimit(10001)

n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# dp[i][j] : 해당 위치로 갈 수 있는 경로 개수
dp = [
    [-1] * m
    for _ in range(n)
]

# 현재 좌표와 그 높이
# 다음 행선지는 현재 높이보다 낮은 곳만 이동 가능
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

def dfs(x, y, cur_h):
    if x == n-1 and y == m-1:
        return 1
    
    # 이미 해당 좌표로 갈 수 있는 경로가 있으면 그 값을 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    path_cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        if not in_range(nx, ny):
            continue
        
        # 높이가 낮은 곳으로 이동
        if arr[nx][ny] < cur_h:
            path_cnt += dfs(nx, ny, arr[nx][ny])
    
    # 경로 개수 기록
    dp[x][y] = path_cnt
    
    return dp[x][y]
        
ans = dfs(0, 0, arr[0][0])
print(ans)