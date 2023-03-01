from math import gcd

def solution(arrayA, arrayB):
    # 카드 리스트의 제일 처음 수로 배열 내 숫자들 간 최대공약수 계산
    # 두 사람 카드 간 공통 최대공약수가 존재한다면 0
    # 아닐 경우 둘 중 최대값 출력
    
    gcd_a = arrayA[0]
    gcd_b = arrayB[0]
    
    for i in range(1, len(arrayA)):
        gcd_a = gcd(arrayA[i], gcd_a)
        gcd_b = gcd(arrayB[i], gcd_b)

    # 각자의 최대공약수로 상대방을 나눌 수 있는 경우가 있다면 flag_a와 flag_b는 모두 1
    flag_b = 0
    for num in arrayA:
        if num % gcd_b == 0:
            flag_b = 1
    
    flag_a = 0
    for num in arrayB:
        if num % gcd_a == 0:
            flag_a = 1
    
    if flag_a == flag_b == 1:
        return 0
    
    else:
        return max(gcd_a, gcd_b)