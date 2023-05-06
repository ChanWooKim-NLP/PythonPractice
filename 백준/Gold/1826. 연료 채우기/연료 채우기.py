import sys
import heapq

input = sys.stdin.readline

n = int(input())

dist_heap = []
for _ in range(n):
    a, b = map(int, input().split())
    dist_heap.append((a, b))

dist_heap.sort()    

l, p = map(int, input().split())

# 초기 연료
cur_fuel = p
# 답
answer = 0

# 현재 위치에서 방문 가능한 주유소 리스트
can_visit = []
while cur_fuel < l:
    # 현재 주유량에서 갈 수 있는 주유소를 모두 tank_heap으로 push
    while dist_heap and dist_heap[0][0] <= cur_fuel:
        loc, tank = heapq.heappop(dist_heap)
        
        # 최대 힙으로 구현하기 위해 주유량을 음수로 heappush
        heapq.heappush(can_visit, -tank)
    
    # 만약 tank_heap이 비어있다면 더 이상 갈 수 없음
    if not can_visit:
        answer = -1
        break
    
    # 가장 많은 주유가 가능한 주유소로 방문
    answer += 1
    cur_fuel -= heapq.heappop(can_visit)

# 방문의 중단이 없고, 전체 주유량이 마을까지의 거리보다 크거나 같을 경우
if answer != -1 and cur_fuel >= l:
    print(answer)

else: print(-1)