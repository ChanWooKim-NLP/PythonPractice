n = int(input())

triangle = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0] * n
    for _ in range(n)
]

# 최종 출력할 최대값, 초기값은 삼각형 맨 위 값
max_val = triangle[0][0]

# 동적 배열 초기화
dp[0] = [0] * n
dp[0][0] = triangle[0][0]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + triangle[i][0]
    dp[i][i] = dp[i-1][i-1] + triangle[i][i]
    
    # 최대값 갱신
    max_val = max(max_val, dp[i][0], dp[i][i])


for i in range(1, n):
    for j in range(1, i):
        # 왼쪽 대각선 위, 오른쪽 대각선 위에서 값 계산
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        
        max_val = max(max_val, dp[i][j])

print(max_val)