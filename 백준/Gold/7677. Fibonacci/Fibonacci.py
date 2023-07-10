import sys

input = sys.stdin.readline

def mul_matrix(arr1, arr2):
    new_arr = [
        [0, 0],
        [0, 0]
    ]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                new_arr[i][j] += arr1[i][k] * arr2[k][j]
            
            new_arr[i][j] %= 10000
            
    return new_arr

def npow_matrix(n, arr):
    if n == 1:
        return arr
    
    if n % 2 == 1:
        powered_matrix = npow_matrix(n-1, arr)
        return mul_matrix(powered_matrix, arr)
    
    else:
        powered_matrix = npow_matrix(n//2, arr)
        return mul_matrix(powered_matrix, powered_matrix)

base = [
    [1, 1],
    [1, 0]
]
while True:
    n = int(input())
    if n == -1:
        break
    
    if n == 0:
        print(0)
        
    else:
        npow = npow_matrix(n, base)
        print(npow[0][1])