import sys

input = sys.stdin.readline

T = int(input())

result = 0
for _ in range(T):
    n = int(input())
    s, t = map(int, input().split())
    cnt = 1

    ans = 0
    while n > 0:
        if n % 2 == 1:
            # 홀수면 2배 복사 후 하나를 더 씀
            n -= 1
            ans += s
            
        else:
            # 하나하나 치는 경우와 현재 메시지 기준 2배 복사하는 비용 비교
            # n*s = 하나하나 쳐서 2배로 만드는 비용
            # t = 2배로 복사하는 비용
            n //= 2
            ans += min(n*s, t)
            
    print(ans)