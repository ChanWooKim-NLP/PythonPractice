import sys

n, k = map(int, sys.stdin.readline().split())

medals = []
for _ in range(n):
    medal_info = list(map(int, sys.stdin.readline().split()))
    medals.append(medal_info)

medals.sort(key=lambda x: (-x[1], -x[2], -x[3]))

result = {}

idx = 1
same = 1
result[medals[0][0]] = 1
for i in range(1, n):
    if medals[i][1:] != medals[i-1][1:]:
        idx += same
        same = 1
    
    else:
        same += 1
        
    result[medals[i][0]] = idx

print(result[k])