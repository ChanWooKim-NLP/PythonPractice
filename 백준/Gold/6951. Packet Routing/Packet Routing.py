import sys

input = sys.stdin.readline

n, w, p = map(int, input().split())
arr = [
    [float('inf')] * (n+1)
    for _ in range(n+1)
]

for i in range(1, n+1):
    arr[i][i] = 0

for _ in range(w):
    a, b, c = map(int, input().split())
    arr[a][b] = c
    arr[b][a] = c
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
            
for _ in range(p):
    a, b = map(int, input().split())
    print(arr[a][b])