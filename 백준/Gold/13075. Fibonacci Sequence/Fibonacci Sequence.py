import sys

input = sys.stdin.readline

def multiple_matrix(arr1, arr2):
    new_arr = [
        [0] * 2
        for _ in range(2)
    ]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                new_arr[i][j] += arr1[i][k] * arr2[k][j]
        
            new_arr[i][j] %= 10**9
    
    return new_arr

def npow_matrix(arr, n):
    if n == 1:
        return arr
    
    if n % 2 == 0:
        pow_matrix = npow_matrix(arr, n//2)
        return multiple_matrix(pow_matrix, pow_matrix)
    
    else:
        pow_matrix = npow_matrix(arr, n-1)
        return multiple_matrix(pow_matrix, arr)
    
n = int(input())

matrix = [
    [1, 1],
    [1, 0]
]
for _ in range(n):
    i = int(input())
    
    pow_matrix = npow_matrix(matrix, i)
    print(pow_matrix[0][1])
