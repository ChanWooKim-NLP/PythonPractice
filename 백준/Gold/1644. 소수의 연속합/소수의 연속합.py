n = int(input())

prime_nums = [1] * (n+1)

for i in range(2, int(n**0.5) + 1):
    if prime_nums[i] == 1:
        for j in range(i*i, n+1, i):
            prime_nums[j] = 0
            

prime_nums_list = [i for i in range(2, n+1) if prime_nums[i] == 1]

def find_prime_sum(n):
    if n == 1:
        return 0
    
    left, right = 0, 0
    cur_sum = prime_nums_list[0]
    answer = 0
    while right < len(prime_nums_list):
        if cur_sum == n:
            answer += 1
            cur_sum -= prime_nums_list[left]
            left += 1
            
        elif cur_sum > n:
            cur_sum -= prime_nums_list[left]
            left += 1
            
        else:
            right += 1
            # 범위를 넘긴다면 반복문 종료
            if right == len(prime_nums_list): break
            cur_sum += prime_nums_list[right]
    
    return answer

answer = find_prime_sum(n)
print(answer)