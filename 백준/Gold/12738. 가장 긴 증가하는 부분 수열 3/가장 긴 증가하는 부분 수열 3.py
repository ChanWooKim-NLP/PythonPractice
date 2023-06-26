import sys

input = sys.stdin.readline

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
            
        else:
            result = mid
            right = mid - 1
            
    return result

n = int(input())

arr = list(map(int, input().split()))

dp = [arr[0]]
for num in arr:
    if num > dp[-1]:
        dp.append(num)
        
    else:
        idx = binary_search(dp, num)
        dp[idx] = num
        
print(len(dp))