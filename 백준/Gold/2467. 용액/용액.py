import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

# 투 포인터 이전 배열 정렬
arr.sort()

min_val = float('inf')
answer = [0, 0]

left, right = 0, n-1

while left < right:
    sum_val = arr[left] + arr[right]
    
    if abs(sum_val) < min_val:
        min_val = abs(sum_val)
        answer = [arr[left], arr[right]]
        
    if sum_val < 0:
        left += 1
        
    else:
        right -= 1
        
print(answer[0], answer[1])