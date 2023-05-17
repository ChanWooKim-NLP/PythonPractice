from collections import defaultdict, deque

arr = [
    list(map(int, input().split()))
    for _ in range(3)
]

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def check_sorted(arr):
    val = 1
    for i in range(3):
        for j in range(3):
            if arr[i][j] != val:
                return False
            
            val += 1
            val %= 9

    return True

def find_zero(arr):
    zero_x, zero_y = 0, 0
    
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0:
                zero_x, zero_y = i, j
    
    return (zero_x, zero_y)

# 해시가 가능하도록 리스트 형식 배열 -> 튜플 형식 배열로 전환
def to_hashable(arr):
    hashable_arr = tuple(map(tuple, arr))
    return hashable_arr

def bfs():    
    visited = defaultdict(int)
    
    queue = deque([(arr, 0)])
    hashable_arr = to_hashable(arr)
    visited[hashable_arr] = 1
    
    while queue:
        cur_arr, cnt = queue.popleft()
        
        if check_sorted(cur_arr):
            return cnt
        
        x, y = find_zero(cur_arr)
        
        # 이동 가능 방향 개수
        for idx in range(4):
            nx, ny = x + dxs[idx], y + dys[idx]
            
            if not (0 <= nx < 3 and 0 <= ny < 3):
                continue

            new_arr = [row[:] for row in cur_arr]
            new_arr[x][y], new_arr[nx][ny] = new_arr[nx][ny], new_arr[x][y]
                        
            hashable_arr = to_hashable(new_arr)
            
            if not visited[hashable_arr]:
                queue.append((new_arr, cnt+1)) # type: ignore
                visited[hashable_arr] = 1
    
    return -1

answer = bfs()
print(answer)
