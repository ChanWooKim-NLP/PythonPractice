
# 본대를 배열로 구현
# 인덱스 0부터 정 -> 전 -> 미 -> 신 -> 한 -> 진 -> 학 -> 형남공학관 
campus = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

def multiple_matrix(arr1, arr2):
    multiplied_arr = [
        [0] * 8
        for _ in range(8)
    ]
    
    for i in range(8):
        for j in range(8):
            for k in range(8):
                multiplied_arr[i][j] += arr1[i][k] * arr2[k][j]
            
            multiplied_arr[i][j] %= 1000000007
            
    return multiplied_arr

def npow_matrix(arr, n):
    if n == 1:
        return arr
    
    if n % 2 == 1:
        powered_matrix = npow_matrix(arr, n-1)
        return multiple_matrix(powered_matrix, arr)
    
    else:
        powered_matrix = npow_matrix(arr, n//2)
        return multiple_matrix(powered_matrix, powered_matrix)

n = int(input())

powered_matrix = npow_matrix(campus, n)
print(powered_matrix[0][0])