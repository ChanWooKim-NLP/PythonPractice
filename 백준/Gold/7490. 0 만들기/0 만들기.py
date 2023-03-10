from collections import deque

def backtracking(idx, target_n, num_list, arr=[]):
    if idx == target_n:
        eq = ''
        for i in range(len(arr)):
            eq += num_list[i] + arr[i]
        
        eq += num_list[-1]
        
        # 큐로 바꾸어 숫자, 피연산자 리스트로 분할
        operand, operator = to_int_equation(eq)
        result = calculate(operand, operator)
        if result == 0:
            print(eq)
        return
    
    operator = [' ', '+', '-']

    for i in range(len(operator)):
        arr.append(operator[i])
        backtracking(idx+1, target_n, num_list, arr)
        arr.pop()

# 문자열 식을 숫자와 연산자 리스트로 분할
def to_int_equation(equation):
    equation = deque(equation)
    operand = []
    operator = []
    
    num = ''
    while equation:
        dq = equation.popleft()
        
        if dq not in ['+', '-', ' ']:
            num += dq
            
        else:
            if dq == ' ':
                continue
            
            else:
                operand.append(int(num))
                operator.append(dq)
                num = ''
    
    # 마지막 항을 피연산자 리스트에 추가
    operand.append(int(num))
    
    return operand, operator
        
def calculate(operand, operator):
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
            
        else:
            result -= operand[i+1]
    
    return result


t = int(input())

for _ in range(t):
    n = int(input())
    
    num_list = list(map(str, range(1, n+1)))
    backtracking(0, n-1, num_list)
    print()