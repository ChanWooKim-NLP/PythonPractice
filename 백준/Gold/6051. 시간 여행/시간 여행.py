import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

# 지금까지의 문제 목록 -> 과거로 돌아가기 위해 사용
history = defaultdict(list)

# 현재 시점의 문제 목록
stack = []

for i in range(1, n+1):
    query = input().split()
    
    if query[0] == 's':
        if stack:
            stack.pop()
        
        if stack:
            print(stack[-1])
            
        else: print(-1)
        
    elif query[0] == 'a':
        # 문제 번호
        problem_num = int(query[1])
        stack.append(problem_num)
        
        print(stack[-1])
        
    else:
        back_time = int(query[1])
        
        # 문제 목록을 해당 시점 바로 이전으로 갱신
        if history[back_time-1]:
            # 깊은 복사
            stack = history[back_time-1][:]
            
        else:
            stack = []
            
        if stack:
            print(stack[-1])
            
        else: print(-1)
        
    # 현재 시점의 문제 기록 저장
    history[i] = stack[:]
    

