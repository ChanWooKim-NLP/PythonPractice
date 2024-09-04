equation = input()

equation = equation.split('-')

answer = 0

for idx, num in enumerate(equation):
    if '+' in num:
        sub_sum = sum(list(map(int, num.split('+')))) # +로 이루어진 부분식의 합을 구함
        
        if idx != 0:
            answer -= sub_sum
            
        else:
            answer += sub_sum
    
    else:
        if idx != 0:
            answer -= int(num)
        
        else:
            answer += int(num)
                
print(answer)