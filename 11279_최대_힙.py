import heapq, sys

# 파이썬 우선순위 큐를 이용
def solution():
    result = []
    queue = []
    N = int(sys.stdin.readline())
    
    for _ in range(N):
        # 오름차순으로 정렬하기 위해 음수로 저장
        x = -int(sys.stdin.readline())
        
        if x == 0:
            if not queue:
                result.append(0)
            
            else:
                # 음수로 저장된 값을 절대값으로 양수화
                val = abs(heapq.heappop(queue))
                result.append(val)
                
        else:
            heapq.heappush(queue, x)
            
    for i in result:
        print(i)
        
solution()
