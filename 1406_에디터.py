import sys

def solution():
    # 커서를 기준으로 스택을 나눔
    stack_1 = list(sys.stdin.readline().strip())
    stack_2 = []
    
    cnt_cmd = int(sys.stdin.readline())
    for _ in range(cnt_cmd):
        cmd = sys.stdin.readline().split()
        
        if cmd[0] == 'L':
            # 커서 이전 문자열이 존재할 경우 커서를 뒤로 이동
            if stack_1:
                stack_2.append(stack_1.pop())
                
        elif cmd[0] == 'D':
            # 커서 이후 문자열이 존재할 경우 커서를 앞으로 이동
            if stack_2:
                stack_1.append(stack_2.pop())
                
        elif cmd[0] == 'B':
            # 커서 바로 이전 문자 삭제
            if stack_1:
                stack_1.pop()
    
        else:
            stack_1.append(cmd[1])
    
    stack_1.extend(stack_2[::-1])
    return ''.join(stack_1)

print(solution())
