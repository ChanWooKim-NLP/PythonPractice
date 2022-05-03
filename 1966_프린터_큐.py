import sys
from collections import deque

def solution():
    case = int(sys.stdin.readline())

    result = []
    for _ in range(case):
        N, M = map(int, sys.stdin.readline().split())
        priority = list(map(int, sys.stdin.readline().split()))
        
        if N == 1:
            result.append(1)
            continue
        
        queue = deque([(idx, p) for idx, p in enumerate(priority)])

        priority.sort()
        
        print_idx = 1
        
        while queue:
            doc = queue.popleft()
            
            if doc[1] == max(priority):
                if doc[0] == M:
                    result.append(print_idx)
                    break
                
                else:
                    print_idx += 1
                    priority.pop()

            else:
                queue.append(doc)
            
    for i in result:
        print(i)
        
solution()
