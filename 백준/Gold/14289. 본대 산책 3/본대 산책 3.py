import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [
    [0] * n
    for _ in range(n)
]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

time = int(input())

def multiple_matrix(arr1, arr2):
    multiplied_arr = [
        [0] * n
        for _ in range(n)
    ]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                multiplied_arr[i][j] += arr1[i][k] * arr2[k][j]
            
            multiplied_arr[i][j] %= 1000000007
            
    return multiplied_arr

def npow_matrix(arr, time):
    if time == 1:
        return arr
    
    if time % 2 == 1:
        powered_matrix = npow_matrix(arr, time-1)
        return multiple_matrix(powered_matrix, arr)
    
    else:
        powered_matrix = npow_matrix(arr, time//2)
        return multiple_matrix(powered_matrix, powered_matrix)

result = npow_matrix(arr, time)
print(result[0][0])