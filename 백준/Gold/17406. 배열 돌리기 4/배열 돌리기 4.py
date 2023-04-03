from copy import deepcopy

# 회전할 수 없는 범위
def not_in_range(x, y, rng, r, c):
    return x > (r+rng-1) or x < (r-rng-1) or y > (c+rng-1) or y < (c-rng-1)

# start_x, start_y : 회전 시작 위치
# arr : 회전할 배열
# r, c, s : 중심 위치와 연산을 수행할 좌표 범위
# rng : 중심 위치에서 떨어진 범위
def rotate(start_x, start_y, rng, arr, r, c, s):
    # 회전 범위를 벗어나면 끝
    if rng == s+1:
        return
    
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    cur_dir = 0
    temp = arr[start_x][start_y]
        
    x, y = start_x, start_y+1
    while True:
        if (x, y) == (start_x, start_y):
            arr[x][y] = temp
            break
        
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        if not_in_range(nx, ny, rng, r, c):
            cur_dir += 1
            continue
        
        arr[x][y], temp = temp, arr[x][y]
        
        x, y = nx, ny

    rotate(start_x-1, start_y-1, rng+1, arr, r, c, s)
    return

# 배열의 최소값 구하는 함수
def calcul_min_arr(arr):
    global ans
    for i in range(len(arr)):
        val = 0
        for j in range(len(arr[0])):
            val += arr[i][j]
        
        ans = min(ans, val)
    return

n, m, k = map(int, input().split())

original_arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 회전 순서를 정하는 백트래킹 함수
order = []
visited = [0] * k
order_comb = []
def backtracking(order_cnt):
    # 회전 순서가 정해지면 rotate 수행
    if order_cnt == k:
        # 원본 배열 복사
        arr = deepcopy(original_arr)

        for center in order_comb:
            # 인덱스는 0부터 시작 (r-1, c-1)
            # 정가운데는 회전을 하지 않기 때문에 (r-1, c-1)에서 시작
            r, c, s = center
            rotate(r-2, c-2, 1, arr, r, c, s)
        
        # 회전한 배열로부터 최소값 구하기
        calcul_min_arr(arr)
        return
    
    for i in range(k):
        if not visited[i]:
            order_comb.append(order[i])
            visited[i] = 1
            
            backtracking(order_cnt+1)
            
            visited[i] = 0
            order_comb.pop()

for _ in range(k):
    r, c, s = map(int, input().split())
    order.append((r, c, s))

ans = float('inf')
backtracking(0)

print(ans)

