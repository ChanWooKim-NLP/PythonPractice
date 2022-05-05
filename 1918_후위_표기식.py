def solution():
    infix = input()
    
    # 결과물을 담을 스택
    outstack = []
    # 연산자 스택, 연산의 순서
    opstack = []
    
    # 
    operand = {
        '+' : 1,
        '-' : 1,
        '*' : 2,
        '/' : 2
    }
    
    for token in infix:
        if token == '(':
            opstack.append(token)
            
        elif token == ')':
            while True:
                pop = opstack.pop()
                if pop == '(':
                    break
                outstack.append(pop)

        elif token in '+-*/':
            while opstack:
                pop = opstack[-1]
                if pop == '(':
                    break
                
                else:
                    if operand[pop] >= operand[token]:
                        outstack.append(opstack.pop())
                    
                    else:
                        break
 
            opstack.append(token)

        else:
            outstack.append(token)
    
    outstack += opstack[::-1]
    
    return ''.join(outstack)

print(solution())
