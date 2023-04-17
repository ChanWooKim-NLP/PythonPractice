n, b = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def mul_matrix(arr1, arr2):
    mul_arr = [
        [0] * n
        for _ in range(n)
    ]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mul_arr[i][j] += arr1[i][k] * arr2[k][j]
            
            # 모든 원소는 1000으로 나눈 나머지
            mul_arr[i][j] %= 1000
            
    return mul_arr

# 분할 정복을 통해 행렬 n제곱
# n이 홀수라면 1을 빼서 짝수로 만들어 곱한 후 arr 한 번 더 곱해줌
# n이 짝수라면 n을 2로 나누어 분할 정복 형식으로 곱함
def npow(arr, b):
    if b == 1:
        return arr
    
    if b % 2 == 1:
        pow_arr = npow(arr, b-1)
        return mul_matrix(pow_arr, arr)
    
    else:
        pow_arr = npow(arr, b//2)
        return mul_matrix(pow_arr, pow_arr)

pow_arr = npow(arr, b)

for i in range(n):
    for j in range(n):
        print(pow_arr[i][j] % 1000, end=' ')
    print()
