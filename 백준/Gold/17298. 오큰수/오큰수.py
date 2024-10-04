import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

answer = [0] * n

stack = []

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        left_idx = stack.pop()
        answer[left_idx] = arr[i]
    
    stack.append(i)

while stack:
    idx = stack.pop()
    answer[idx] = -1
    
print(*answer)