import sys
from pprint import pprint


input = sys.stdin.readline

# 가장자리 벌 성장
def grow_up_side(side_grow_cnt):
    for i in range(m-1, -1, -1):
        # 가장 왼쪽 열 성장
        grow_up_arr[i][0] += side_grow_cnt[m-i-1]
    
    for j in range(1, m):
        # 가장 윗쪽 행 성장
        grow_up_arr[0][j] += side_grow_cnt[m+j-1]

# 왼쪽, 왼쪽 위, 위에서 가장 많이 성장한 애벌레의 성장 크기 찾기
dxs, dys = [0, -1, -1], [-1, -1, 0]
def _find_surrounding_max_grow(x, y):
    max_size = 0
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        max_size = max(max_size, grow_up_arr[nx][ny])
        
    return max_size

# 주변에서 가장 많이 성장한 애벌레의 크기를 배열에 기록
def grow_up_per_day():
    for i in range(1, m):
        for j in range(1, m):
            max_size_from_surround = _find_surrounding_max_grow(i, j)
            grow_up_arr[i][j] += max_size_from_surround

m, n = map(int, input().split())

honeycomb = [
    [1] * m
    for _ in range(m)
]

for _ in range(n):
    # 가장자리 벌들이 성장하는 크기
    side_grow_cnt = []
    
    # 가장자리가 성장하는 0/1/2의 개수
    grow_arr = list(map(int, input().split()))
    
    # 각 위치 별 성장 크기로 매핑 (2m-1개)
    for i in range(3):
        for cnt in range(grow_arr[i]):
            side_grow_cnt.append(i)
    
    # 각 벌 당 성장 크기 배열
    grow_up_arr = [
        [0] * m
        for _ in range(m)
    ]
    
    grow_up_side(side_grow_cnt)
    grow_up_per_day()
    
    for i in range(m):
        for j in range(m):
            honeycomb[i][j] += grow_up_arr[i][j]
            
for i in range(m):
    for j in range(m):
        print(honeycomb[i][j], end=' ')
    print()