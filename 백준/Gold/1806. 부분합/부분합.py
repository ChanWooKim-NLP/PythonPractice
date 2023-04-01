n, target = map(int, input().split())

arr = list(map(int, input().split()))

right = 0
sum = 0

ans = float('inf')

for left in range(n):
    while sum < target and right < n:
        sum += arr[right]
        right += 1
        
    if sum >= target:
        ans = min(ans, right-left)
    
    sum -= arr[left]

if ans == float('inf'):
    print(0)
else:
    print(ans)