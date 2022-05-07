import heapq

def solution():
    queue = []
    N = int(input())
    dasom_vote = -int(input())
    
    for _ in range(N-1):
        vote = int(input())
        # 음수로 변환하여 오름차순으로 반환 (heapq는 낮은 숫자 순서로 반환하기 때문)
        heapq.heappush(queue, -vote)
    
    answer = 0
    while queue:
        temp = heapq.heappop(queue)
        
        if temp <= dasom_vote:
            temp += 1
            # 뺏은 표 추가
            answer += 1
            dasom_vote -= 1
            # 다시 큐에 추가
            heapq.heappush(queue, temp)
        
        else:
            break
    
    return answer

print(solution())
