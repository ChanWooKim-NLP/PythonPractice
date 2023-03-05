from math import sqrt, floor

def prime_num(n):
    root = floor(sqrt(n))
    for i in range(2, root+1):
        if n % i == 0:
            return False
        
    return True

def to_digit(n, k):
    result = ''
    
    while n > 0:
        n, mod = n // k, n % k
        result += str(mod)
    
    return result[::-1]

def solution(n, k):
    digit_num = to_digit(n, k)
    
    print(digit_num)
    
    num_split = digit_num.split('0')
    print(num_split)
    
    prime_list = []
    
    for num in num_split:
        if num != '1' and num != '':
            num = int(num)
            
            if prime_num(num):
                prime_list.append(num)
                
    print(prime_list)
    answer = len(prime_list)
    return answer

