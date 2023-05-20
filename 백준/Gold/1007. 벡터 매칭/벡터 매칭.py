import sys
from itertools import combinations
from math import sqrt

input = sys.stdin.readline

# 백트래킹을 이용하여 벡터 그룹을 생성
# 벡터의 시작점에서 각 좌표를 더한 값과 끝 점의 각 좌표 더한 값
# 두 값을 뺀 값이 이루는 벡터 크기가 최소 -> 정답
t = int(input())

for _ in range(t):
    n = int(input())
    
    vectors = []
    x_sum, y_sum = 0, 0
    for _ in range(n):
        x, y = map(int, input().split())
        # 이 값에서 벡터의 시작점의 합을 뺀 값이 끝 점의 합
        x_sum += x
        y_sum += y
        vectors.append((x, y))
    
    # 벡터 그룹 생성 후 사이즈 비교
    min_size = float('inf')
    
    selected_vectors = list(combinations(vectors, n//2))
    for combination in selected_vectors[:len(selected_vectors)//2]:
        x_start_sum, y_start_sum = 0, 0
        
        for sub_x, sub_y in combination:
            x_start_sum += sub_x
            y_start_sum += sub_y
            
        x_end_sum = x_sum - x_start_sum
        y_end_sum = y_sum - y_start_sum
        
        v_size = sqrt((x_end_sum-x_start_sum)**2 + (y_end_sum-y_start_sum)**2)
        
        if v_size < min_size:
            min_size = v_size
            
    print(min_size)