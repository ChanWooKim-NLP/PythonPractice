import sys

n, m = map(int, sys.stdin.readline().split())

arr = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

prefix_sum = [
    [0] * (m+1)
    for _ in range(n+1)
]

# 2차원 누적합
for i in range(1, n+1):
    for j in range(1, m+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i-1][j-1]

k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]

    print(answer)