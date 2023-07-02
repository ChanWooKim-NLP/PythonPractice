import sys
import bisect

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
        
    dp = [arr[0]]

    for num in arr:
        if num > dp[-1]:
            dp.append(num)
            
        else:
            idx = bisect.bisect_left(dp, num)
            dp[idx] = num
    
    print(len(dp))
    
