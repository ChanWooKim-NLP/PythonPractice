from collections import defaultdict

def solution():
    num_dict = defaultdict(int)
    
    N = int(input())
    expression = input()
    
    stack = []
    
    for s in expression:
        if s not in '+-*/' and not num_dict[s]:
            num = int(input())
            num_dict[s] = num
    
    for s in expression:
        if s in '+-*/':
            num_1 = stack.pop()
            num_2 = stack.pop()
            
            if s == '+':
                val = num_1 + num_2
            
            elif s == '-':
                val = num_2 - num_1
                
            elif s == '*':
                val = num_1 * num_2

            else:
                val = num_2 / num_1

            stack.append(val)
        
        else:
            stack.append(num_dict[s])
    
    return format(stack[0], '.2f')
    
print(solution())
