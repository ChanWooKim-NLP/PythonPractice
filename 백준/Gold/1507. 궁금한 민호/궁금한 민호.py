import sys

input = sys.stdin.readline

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

origin_path = [
    [1] * n
    for _ in range(n)
]

can_restore = True
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or i == k or k == j:
                continue
            
            if arr[i][k] + arr[k][j] == arr[i][j]:
                origin_path[i][j] = 0

            elif arr[i][k] + arr[k][j] < arr[i][j]:
                can_restore = False
                
if can_restore:
    answer = 0
    for i in range(n):
        for j in range(i+1, n):
            if origin_path[i][j]:
                answer += arr[i][j]
    
    print(answer)
    
else:
    print(-1)
            