import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

heapq.heapify(cards)

for _ in range(m):
    min_sum = 0
    for _ in range(2):
        min_sum += heapq.heappop(cards)
        
    for _ in range(2):
        heapq.heappush(cards, min_sum)
        
print(sum(cards))