n, m = map(int, input().split())

num = list(map(int, input().split()))

num.sort()

visited = [0] * n

answer = []
def backtracking(cnt=0):
    if cnt == m:
        for i in answer:
            print(i, end=' ')
        print()
        return
    
    for i in range(n):
        if visited[i]:
            continue
        
        visited[i] = 1
        answer.append(num[i])
        
        backtracking(cnt+1)
        
        answer.pop()
        visited[i] = 0
        
backtracking(0)