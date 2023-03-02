from collections import deque

def solution(priorities, location):
    priorities_queue = deque(priorities)
    document_idx = deque(range(len(priorities)))
        
    answer = 1
    while priorities_queue:
        document = priorities_queue.popleft()
        idx = document_idx.popleft()
        
        can_print = True
        for i in range(len(priorities_queue)):
            if priorities_queue[i] > document:
                priorities_queue.append(document)
                document_idx.append(idx)
                
                can_print = False
                break
                
        if can_print:
            if idx == location:
                return answer
            
            else:
                answer += 1