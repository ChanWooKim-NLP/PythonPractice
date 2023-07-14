import sys
import string

input = sys.stdin.readline

n = int(input())

STRING_SET = string.ascii_lowercase + string.ascii_uppercase
string_idx = {
    s:idx for idx, s in enumerate(STRING_SET)
}

idx_to_string = {
    idx:s for idx, s in enumerate(STRING_SET)
}

arr = [
    [0] * 52
    for _ in range(52)
]
for _ in range(n):
    pre_prop, post_prop = input().strip('\n').split(' => ')
    pre_idx, post_idx = string_idx[pre_prop], string_idx[post_prop]
    
    arr[pre_idx][post_idx] = 1

for k in range(52):
    for i in range(52):
        for j in range(52):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

result = []
for i in range(52):
    for j in range(52):
        if arr[i][j] and (i != j):
            pre, post = idx_to_string[i], idx_to_string[j]
            result.append((pre, post))
            
result.sort(key=lambda x: (x[0], x[1]))
print(len(result))
for r in result:
    print(f'{r[0]} => {r[1]}')