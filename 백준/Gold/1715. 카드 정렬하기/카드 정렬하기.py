import heapq

n = int(input())

heap = []
for _ in range(n):
    card = int(input())
    heapq.heappush(heap, card)

# n이 1이라면 비교할 대상이 없음
if n == 1:
    print(0)

else:
    result = 0

    # 힙에서 최소값을 2번 더해주고, result에 더한 후 다시 힙에 집어넣어 줌
    # 예) 10 20 40일 때, 10+20을 result에 추가하고 10+20을 heap에 삽입 -> (30, 40)
    # 30 + 30 + 40 = 100
    # 힙의 길이가 1이면 계산이 끝난 것
    while len(heap) != 1:
        card_merge = 0
        for _ in range(2):
            card_merge += heapq.heappop(heap)
        
        result += card_merge
        heapq.heappush(heap, card_merge)
    
    print(result) 