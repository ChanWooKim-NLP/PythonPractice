string = input()
explosion = input()

def check_exp(explosion):
    # 폭발 확인할 스택 내 문자열
    sub_s = stack[-len(explosion):]
    for s in range(len(explosion)):
        if sub_s[s] != explosion[s]:
            return
        
    for _ in range(len(explosion)):
        stack.pop()

    return

# 스택에 쌓아두면서 탐색
# 마지막에 들어간 문자와 폭발 대상 문자의 마지막 글자가 같다면 탐색
stack = []
for s in string:
    stack.append(s)

    if s == explosion[-1] and len(stack) >= len(explosion):
        check_exp(explosion)
    
if stack:
    print(''.join(stack))
    
else:
    print('FRULA')