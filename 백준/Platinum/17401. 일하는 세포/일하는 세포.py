import sys

input = sys.stdin.readline

t, n, d = map(int, input().split())

matrix_list = []
for _ in range(t):
    matrix = [
        [0] * n
        for _ in range(n)
    ]
    
    m = int(input())
    for _ in range(m):
        a, b, c = map(int, input().split())
        matrix[a-1][b-1] = c
        
    matrix_list.append(matrix)
    
def multiple_matrix(arr1, arr2):
    new_matrix = [
        [0] * n
        for _ in range(n)
    ]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_matrix[i][j] += arr1[i][k] * arr2[k][j]
                
            new_matrix[i][j] %= 1000000007
            
    return new_matrix

def npow_matrix(cnt, arr):
    if cnt == 0:
        base_matrix = [
            [0] * n
            for _ in range(n)
        ]
        for i in range(n):
            base_matrix[i][i] = 1
        
        return base_matrix
    
    if cnt == 1:
        return arr
    
    if cnt % 2 == 1:
        pow_matrix = npow_matrix(cnt-1, arr)
        return multiple_matrix(pow_matrix, arr)
    
    else:
        pow_matrix = npow_matrix(cnt//2, arr)
        return multiple_matrix(pow_matrix, pow_matrix)

def solution():
    pow_cnt = d // t

    # 각 독립된 지도를 곱한 후, pow_cnt만큼 제곱
    # 제곱한 후에는 d % t번만큼 각 주기의 지도 행렬을 곱함
    base_matrix = [
        [0] * n
        for _ in range(n)
    ]
    for i in range(n):
        base_matrix[i][i] = 1
        
    for map_matrix in matrix_list:
        base_matrix = multiple_matrix(base_matrix, map_matrix)
        
    pow_matrix = npow_matrix(pow_cnt, base_matrix)

    for i in range(d % t):
        pow_matrix = multiple_matrix(pow_matrix, matrix_list[i])
        
    return pow_matrix

answer = solution()
for i in range(n):
    print(*answer[i])