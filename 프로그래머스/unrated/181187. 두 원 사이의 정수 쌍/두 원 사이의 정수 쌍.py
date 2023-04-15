from math import sqrt, ceil, floor

def solution(r1, r2):
    answer = 0
    
    for x in range(1, r2+1):
        min_y = max(0, r1**2 - x**2)
        min_y = ceil(sqrt(min_y))
        
        max_y = floor(sqrt(r2**2 - x**2))
        
        dot_cnt = max_y - min_y + 1
        answer += dot_cnt
    
    answer *= 4
    
    return answer