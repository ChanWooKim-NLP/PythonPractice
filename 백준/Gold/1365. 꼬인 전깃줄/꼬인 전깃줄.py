import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

dp = [arr[0]]

def binary_search(dp, target):
    left, right = 0, len(dp) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if dp[mid] < target:
            left = mid + 1
            
        else:
            result = mid
            right = mid - 1
    
    return result
    
for num in arr:
    if num > dp[-1]:
        dp.append(num)
        
    else:
        idx = binary_search(dp, num)
        dp[idx] = num

print(n - len(dp))