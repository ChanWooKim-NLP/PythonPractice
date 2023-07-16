import sys

input = sys.stdin.readline

n = int(input())

arr = [(int(input()), i) for i in range(n)]

arr.sort(key=lambda x: x[0])

answer = 0
# 원래 인덱스와 정렬 후 인덱스의 차이 중 최댓값
for i in range(n):
    answer = max(answer, arr[i][1] - i)
    
print(answer+1)