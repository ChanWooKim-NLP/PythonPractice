import sys
input = sys.stdin.readline

v, e = map(int, input().split())
arr = [
    [1e9] * (v+1)
    for _ in range(v+1)
]

for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
            
min_dist = 1e9
for i in range(1, v+1):
    for j in range(1, v+1):
        if i == j:
            continue
        
        if arr[i][j] + arr[j][i] < min_dist:
            min_dist = arr[i][j] + arr[j][i]
            
if min_dist == 1e9:
    print(-1)
    
else:
    print(min_dist)