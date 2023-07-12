import sys

input = sys.stdin.readline

p = int(input())

base_matrix = [
    [1, 1],
    [1, 0]
]

def multiple_matrix(arr1, arr2):
    new_matrix = [
        [0, 0],
        [0, 0]
    ]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                new_matrix[i][j] += arr1[i][k] * arr2[k][j]

            new_matrix[i][j] %= 10**9
            
    return new_matrix

def npow_matrix(arr, n):
    if n == 1:
        return arr
    
    if n % 2 == 0:
        powered_matrix = npow_matrix(arr, n//2)
        return multiple_matrix(powered_matrix, powered_matrix)
    
    else:
        powered_matrix = npow_matrix(arr, n-1)
        return multiple_matrix(powered_matrix, arr)

for _ in range(p):
    i, n = map(int, input().split())
    
    powered_matrix = npow_matrix(base_matrix, n)
    print(i, powered_matrix[0][1])