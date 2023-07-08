n = int(input())

def multiple_matrix(arr1, arr2):
    new_arr = [
        [0, 0],
        [0, 0]
    ]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                new_arr[i][j] += arr1[i][k] * arr2[k][j]
                
            new_arr[i][j] %= 1000000007
            
    return new_arr

def npow_matrix(n, arr):
    if n == 1:
        return arr
    
    if n % 2 == 1:
        powered_matrix = npow_matrix(n-1, arr)
        return multiple_matrix(powered_matrix, arr)
    
    else:
        powered_matrix = npow_matrix(n//2, arr)
        return multiple_matrix(powered_matrix, powered_matrix)

base_matrix = [
    [1, 1],
    [1, 0]
]
powered_matrix = npow_matrix(n, base_matrix)
print(powered_matrix[0][1])