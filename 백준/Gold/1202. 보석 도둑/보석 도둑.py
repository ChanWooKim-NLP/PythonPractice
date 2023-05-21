import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

jw_list = []
for _ in range(n):
    m, v = map(int, input().split())
    # 가격 기준 최대 힙
    heapq.heappush(jw_list, (m, v))
    
weight = []
for _ in range(k):
    c = int(input())
    weight.append(c)

weight.sort()

# 훔칠 수 있는 보석 후보군
steal_jws_candidate = []
answer = 0
for w in weight:
    # 보석 리스트에서 가방에 넣을 수 있는 보석의 가치를 후보군에 추가 
    while jw_list and w >= jw_list[0][0]:
        value = heapq.heappop(jw_list)[1]
        # 최대 힙으로 구현
        heapq.heappush(steal_jws_candidate, -value)
        
    if steal_jws_candidate:
        answer -= heapq.heappop(steal_jws_candidate)
        
print(answer)