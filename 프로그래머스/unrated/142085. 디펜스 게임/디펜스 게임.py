import heapq

def solution(n, k, enemy):    
    # 힙 자료구조를 통해 최대 힙 구현
    # 힙에 추가 : 라운드 진행 의미
    # 라운드를 진행하며 적의 수를 total_enemy에 추가해줌
    # 적의 수가 내가 가진 n보다 많을 경우 k를 소모하고 진행한 라운드에서 pop한 후 answer 추가
    # 내가 가진 병사가 많을 경우 answer 추가
    heap = []
    answer = 0
    total_enemy = 0
    
    for e in enemy:
        heapq.heappush(heap, -e)
        total_enemy += e
        
        if total_enemy > n:
            if k == 0:
                break
            k -= 1
            total_enemy += heapq.heappop(heap)
        
        answer += 1
    
    return answer