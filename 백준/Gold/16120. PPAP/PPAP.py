s = list(input())

stack = []

def check():
    if ''.join(stack[-4:]) == 'PAPP':
        for _ in range(4):
            stack.pop()
        
        stack.append('P')

while s:
    stack.append(s.pop())
    
    if len(stack) >= 4:
        check()
        
if len(stack) == 1 and stack[0] == 'P':
    print('PPAP')
    
else:
    print('NP')