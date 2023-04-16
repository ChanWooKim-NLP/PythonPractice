n, k = map(int, input().split())

knapsacks = []
for _ in range(n):
    w, v = map(int, input().split())
    knapsacks.append((w, v))
    

# 전체 물품 개수에 최대 무게에 따라 얻을 수 있는 최대 가치
dp = [
    [0] * (k+1)
    for _ in range(n+1)
]

# i : 물건 순서
# j : 용량
for i in range(1, n+1):
    for j in range(1, k+1):
        # 해당 순서 물건의 무게가 j보다 커 넣을 수 없다면 이전 상태 그대로
        if knapsacks[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        
        # i번째 물건을 넣을 수 있는 경우
        # 새로운 물건을 넣어 가치를 추가한 경우와 이전 상태 비교
        else:
            dp[i][j] = max(dp[i-1][j], 
                           dp[i-1][j - knapsacks[i-1][0]] + knapsacks[i-1][1])
            
print(dp[-1][-1])
            