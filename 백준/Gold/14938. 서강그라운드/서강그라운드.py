n, m, r = map(int, input().split())

item_cnt = list(map(int, input().split()))

graph = [
    [1e9] * n
    for _ in range(n)
]

for _ in range(r):
    a, b, l = map(int, input().split())
    
    graph[a-1][b-1] = l
    graph[b-1][a-1] = l

# 수색이 시작되는 정점은 0으로 설정
for i in range(n):
    graph[i][i] = 0

# 각 정점 별 최단거리 갱신
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
max_item = 0
# 시작지 별 얻을 수 있는 아이템 개수
for start in range(n):
    cnt = 0
    # 해당 정점에서 시작할 경우 거리와 아이템 개수 탐색
    for idx in range(n):
        dist = graph[start][idx]
        
        # 출발지에서 m 이내로 갈 수 있는 거리라면 아이템 획득
        if dist <= m:
            cnt += item_cnt[idx]
    
    # 최대로 얻을 수 있는 아이템 개수 갱신
    if max_item < cnt:
        max_item = cnt

print(max_item)