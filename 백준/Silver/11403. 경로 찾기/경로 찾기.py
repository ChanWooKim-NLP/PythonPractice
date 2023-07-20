import sys

input = sys.stdin.readline

n = int(input())

arr = [
    [float('inf')] * n
    for _ in range(n)
]

for i in range(n):
    path = list(map(int, input().split()))
    
    for j in range(n):
        if path[j] != 0:
            arr[i][j] = path[j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
            
for i in range(n):
    for j in range(n):
        if arr[i][j] != float('inf'):
            print(1, end=' ')
            
        else:
            print(0, end=' ')
    print()