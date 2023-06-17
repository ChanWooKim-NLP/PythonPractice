import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = 0
left, right = 0, 0
visited = [0] * (100001)

while left <= right and right < n:
    # 현재 수열 내 같은 수가 없다면
    if not visited[arr[right]]:
        visited[arr[right]] = 1
        right += 1
        answer += (right - left)
    
    # 같은 수가 존재한다면 left를 1 늘려야 하므로 방문 배열 조정 
    else:
        visited[arr[left]] = 0
        left += 1
    
print(answer)