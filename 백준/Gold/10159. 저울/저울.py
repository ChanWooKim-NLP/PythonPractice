from collections import defaultdict

n = int(input())
m = int(input())

# 방향 그래프
graph = defaultdict(list)

# 거리 기록 배열
dist = [
    [float('inf')] * (n+1)
    for _ in range(n+1)
]

# 비교 여부 배열
compare = [
    [0] * (n+1)
    for _ in range(n+1)
]

for _ in range(m):
    heavy, light = map(int, input().split())
    
    graph[heavy].append(light)
    dist[heavy][light] = 1

# 다른 물건을 거쳐 해당 물건의 무게와 비교할 수 있는가?
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            
            # 비교가 된다면 비교 여부 배열에 기록
            if dist[i][j] != float('inf'):
                compare[i][j] = 1
                compare[j][i] = 1
                

for i in range(1, n+1):
    compare_cnt = compare[i].count(1)
    
    # 자기 자신 제외
    ans = n - compare_cnt - 1        
    print(ans)