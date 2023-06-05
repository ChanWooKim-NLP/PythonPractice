import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    arr = [
        [float('inf')] * (n+1)
        for _ in range(n+1)
    ]
    
    for i in range(1, n+1):
        arr[i][i] = 0
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        arr[a][b] = c
        arr[b][a] = c
    
    # 플로이드-워셜 알고리즘
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]
                    
    k = int(input())
    friends = list(map(int, input().split()))
    
    min_dist = float('inf')
    # 이동 거리가 최소가 되는 방 번호
    target_room = 0
    
    for i in range(1, n+1):
        total_dist = 0
        for f_idx in friends:
            total_dist += arr[i][f_idx]
            
        if total_dist < min_dist:
            min_dist = total_dist
            target_room = i
            
    print(target_room)