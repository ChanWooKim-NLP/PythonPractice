n = int(input())

lines = list(map(int, input().split()))

real_lines = [0] * n
for i in range(n):
    current = lines[i]
    cnt = 0

    for j in range(n):
        if cnt == current and real_lines[j] == 0:
            real_lines[j] = i+1
            break
        
        elif real_lines[j] == 0:
            cnt += 1
            
print(*real_lines)