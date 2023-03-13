import sys, heapq

input = sys.stdin.readline

n = int(input())

lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 시작점과 끝점 기준 정렬
lines.sort(key=lambda x: x[0])

# 끝 점만 저장하는 최소 힙
heap = [
    lines[0][1]
]

overlap = 1
cur_s, cur_e = lines[0]
for idx in range(1, n):
    s, e = lines[idx]
    
    # 힙에서 겹치지 않는 선분의 끝 점 빼내기
    # 시작점이 선분의 끝 점이랑 같거나, 크면 겁치지 않는 것
    while heap and s >= heap[0]:
        heapq.heappop(heap)
        
    heapq.heappush(heap, e)
    overlap = max(overlap, len(heap))
        
print(overlap)
