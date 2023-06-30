import sys
import bisect

input = sys.stdin.readline

while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        
        dp = [arr[0]]
        for num in arr:
            if num > dp[-1]:
                dp.append(num)
                
            else:
                idx = bisect.bisect_left(dp, num)
                dp[idx] = num
        
        print(len(dp))
        
    except:
        break