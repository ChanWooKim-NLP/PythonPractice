def solution(n):
    x = int(n**(0.5))
    
    if x**2 != n:
        return -1
    
    else:
        answer = (x+1)**2
        return answer