import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [
    [float('inf')] * (n+1)
    for _ in range(n+1)
]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])

answer = 0
for i in range(1, n+1):
    know_order = True
    
    for j in range(1, n+1):
        if i != j and arr[i][j] == float('inf') and arr[j][i] == float('inf'):
            know_order = False
            break
    
    if know_order:
        answer += 1
        
print(answer)