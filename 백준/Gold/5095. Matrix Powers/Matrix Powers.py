import sys

input = sys.stdin.readline

def multiple_matrix(arr1, arr2):
    new_matrix = [
        [0] * n
        for _ in range(n)
    ]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_matrix[i][j] += arr1[i][k] * arr2[k][j]
                
            new_matrix[i][j] %= m
            
    return new_matrix

def npow_matrix(arr, pow_cnt):
    if pow_cnt == 1:
        return arr
    
    if pow_cnt % 2 == 0:
        powered_matrix = npow_matrix(arr, pow_cnt//2)
        return multiple_matrix(powered_matrix, powered_matrix)
    
    else:
        powered_matrix = npow_matrix(arr, pow_cnt-1)
        return multiple_matrix(powered_matrix, arr)

while True:
    n, m, p = map(int, input().split())
    
    if n == 0 and m == 0 and p == 0:
        break
    
    matrix = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    
    powered_matrix = npow_matrix(matrix, p)
    
    for i in range(n):
        for j in range(n):
            print(powered_matrix[i][j], end=' ')
        print()
    print()