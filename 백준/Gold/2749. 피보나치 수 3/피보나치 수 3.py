n = int(input())

arr = [
    [1, 1],
    [1, 0]
]

def matrix_multiple(arr1, arr2):
    multiplied_arr = [
        [0, 0],
        [0, 0]
    ]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                multiplied_arr[i][j] += arr1[i][k] * arr2[k][j]

            multiplied_arr[i][j] %= 1000000
        
    return multiplied_arr

def npow_matrix(arr, cnt):
    if cnt == 1:
        return arr
    
    if cnt % 2 == 0:
        pow_matrix = npow_matrix(arr, cnt//2)
        return matrix_multiple(pow_matrix, pow_matrix)
    
    else:
        pow_matrix = npow_matrix(arr, cnt-1)
        return matrix_multiple(pow_matrix, arr)
    
pow_matrix = npow_matrix(arr, n)

fibo = [0, 1]

fibo_n = pow_matrix[0][0] * fibo[0] + pow_matrix[0][1] * fibo[1]
print(fibo_n % 1000000)