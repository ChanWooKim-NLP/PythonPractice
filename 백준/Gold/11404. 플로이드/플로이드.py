import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

cities = [
    [float('inf')] * (n+1)
    for _ in range(n+1)
]

for _ in range(m):
    a, b, c = map(int, input().split())
    
    # 노선 비용이 등록된 상태에서 더 큰 비용의 같은 노선이 들어온다면 무시
    if cities[a][b] != float('inf') and c > cities[a][b]:
        continue
    
    cities[a][b] = c

# 자기 자신으로 오는 노선은 없으므로 0으로 설정
for i in range(1, n+1):
    cities[i][i] = 0
        
# 플로이드-워셜 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if cities[i][j] > cities[i][k] + cities[k][j]:
                cities[i][j] = cities[i][k] + cities[k][j]

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if cities[i][j] == float('inf'):
            print(0, end=' ')
            
        else:
            print(cities[i][j], end=' ')
            
    print()

    