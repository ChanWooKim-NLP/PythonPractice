import sys

n = int(sys.stdin.readline())

length = list(map(int, sys.stdin.readline().split()))

price = list(map(int, sys.stdin.readline().split()))

total = 0
to_next_city = length[0]
min_price = price[0]

for i in range(1, n-1):
    if price[i] < min_price:
        # 이전 최소 비용과 해당 도시까지 도달하는데 필요한 거리를 곱하여 비용 계산
        total += to_next_city * min_price
        
        # 해당 도시의 기름값으로 최소 비용 갱신
        to_next_city = length[i]
        min_price = price[i]
        
    else:
        to_next_city += length[i]

# 최근 최저가 주요소 도시에서 마지막 도시까지 오는 거리를 계산 
total += min_price * to_next_city

print(total)