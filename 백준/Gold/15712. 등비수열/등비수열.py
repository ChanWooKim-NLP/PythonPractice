a, r, n, mod = map(int, input().split())

def sum_seq(r, n, mod):
    if n == 1:
        return 1
    
    elif n % 2 == 0:
        half_sum = sum_seq(r, n//2, mod)
        return (half_sum * (pow(r, n//2, mod) + 1)) % mod
    
    else:
        half_sum = sum_seq(r, n-1, mod)
        return (half_sum + pow(r, n-1, mod)) % mod

if r == 1:
    print(a*n % mod)
    
else:
    answer = sum_seq(r, n, mod)
    print(a * answer % mod)