def solution(number, k):
    answer = ''
    
    stack = []
    
    cnt = 0
    for i in range(len(number)):
        while stack and number[stack[-1]] < number[i] and cnt < k:
            stack.pop()
            cnt += 1
        
        stack.append(i)
    
    while cnt < k:
        stack.pop()
        cnt += 1
    
    for i in stack:
        answer += number[i]
    
    return answer