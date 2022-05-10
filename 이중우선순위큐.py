import heapq    

def solution(operations):
    heap = []

    for op in operations:
        # 연산자를 공백으로 나누고 기준에 따라 명령 처리
        if op.split()[0] == 'I':
            # 문자열이므로 int 정수화하여 힙에 추가
            heapq.heappush(heap, int(op.split()[1]))

        elif op.split()[0] == 'D' and op.split()[1] == '-1':
            if heap:
                heapq.heappop(heap)
        
        # 최대값을 뽑아내는 과정
        elif op.split()[0] == 'D' and op.split()[1] == '1':
            if heap:
                # nlargest 함수 이용하면 n만큼 최대값을 내림차순으로 출력
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
                
    if heap:
        answer = [max(heap),min(heap)]
    
    else:
        answer = [0,0]
        
    return answer
