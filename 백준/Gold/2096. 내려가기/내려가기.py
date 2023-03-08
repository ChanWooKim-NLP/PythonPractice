import sys

input = sys.stdin.readline

n = int(input())

# [max_dp, min_dp]
first_vals = list(map(int, input().split()))
dp = [
    first_vals, first_vals
]

for i in range(1, n):
    vals = list(map(int, input().split()))
    
    new_max = [
        max(dp[0][0], dp[0][1]) + vals[0],
        max(dp[0]) + vals[1],
        max(dp[0][1], dp[0][2]) + vals[2],
    ]
    
    new_min = [
        min(dp[1][0], dp[1][1]) + vals[0],
        min(dp[1]) + vals[1],
        min(dp[1][1], dp[1][2]) + vals[2],
    ]
    
    dp[0] = new_max
    dp[1] = new_min
    
print(max(dp[0]), min(dp[1]))