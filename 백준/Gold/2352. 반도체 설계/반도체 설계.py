import sys

input = sys.stdin.readline

# dp를 이진 탐색하며 target 값이 들어갈 위치를 찾음
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

# LIS 배열을 저장
dp = [arr[0]]

for num in arr:
    if num > dp[-1]:
        dp.append(num)
        
    else:
        idx = binary_search(dp, num)
        dp[idx] = num

print(len(dp))
