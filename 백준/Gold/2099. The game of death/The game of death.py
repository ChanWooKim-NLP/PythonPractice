import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())

matrix = [
    [0] * n
    for _ in range(n) 
]

for i in range(n):
    a, b = map(int, input().split())
    matrix[i][a-1] = 1
    matrix[i][b-1] = 1
    
def multiple_matrix(arr1, arr2):
    new_matrix = [
        [0] * n
        for _ in range(n)
    ]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr1[i][k] and arr2[k][j]:
                    new_matrix[i][j] = 1
                
    return new_matrix

def npow_matrix(cnt, arr):
    if cnt == 1:
        return arr
    
    if cnt % 2 == 1:
        powered_matrix = npow_matrix(cnt-1, arr)
        return multiple_matrix(powered_matrix, arr)
    
    else:
        powered_matrix = npow_matrix(cnt//2, arr)
        return multiple_matrix(powered_matrix, powered_matrix)
    
powered_matrix = npow_matrix(k, matrix)

for _ in range(m):
    a, b = map(int, input().split())
    
    if powered_matrix[a-1][b-1]:
        print("death")
        
    else:
        print("life")