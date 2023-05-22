import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [
    [0] * (n+1)
    for _ in range(n+1)
]
    
# 길이가 1인 펠린드림
for i in range(1, n+1):
    dp[i][i] = 1
    
# 길이가 2인 펠린드롬
for i in range(1, n):
    if arr[i-1] == arr[i]:
        dp[i][i+1] = 1

# 그 이상 길이의 펠린드롬
for str_length in range(3, n+1):
    for start in range(1, n-str_length+2):
        end = start + str_length - 1
        
        # 원 문자열의 시작과 끝을 비교 후 그 사이의 문자열이 이미 펠린드롬으로 기록된 경우
        if arr[start-1] == arr[end-1] and dp[start+1][end-1]:
            dp[start][end] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])