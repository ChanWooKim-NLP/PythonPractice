# 처음에 입력하는 두 문자열
a = input()
b = input()

n, m = len(a), len(b)

dp = [
    [0] * (m+1)
    for _ in range(n+1)
]

max_len = 0
lcs = ''
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            
            if dp[i][j] > max_len:
                max_len = dp[i][j]
                lcs += a[i-1]
                
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

lcs_length = dp[-1][-1]
print(lcs_length)

lcs = ''
# 역순으로 올라가며 문자열 추가
x, y = n, m
while x > 0 and y > 0:
    if dp[x][y] == dp[x][y-1]:
        y -= 1
    
    elif dp[x][y] == dp[x-1][y]:
        x -= 1
        
    else:
        lcs += a[x-1]
        x -= 1
        y -= 1

if lcs:  
    print(lcs[::-1])