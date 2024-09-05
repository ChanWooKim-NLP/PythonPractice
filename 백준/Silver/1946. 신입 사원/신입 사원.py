import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    candidates = []
    for _ in range(n):
        resume, interview = map(int, sys.stdin.readline().split())
        candidates.append((resume, interview))

    candidates.sort()
    
    # 무조건 1등은 뽑히므로 1명은 확보
    answer = 1
    
    # 1등의 면접 전형 결과
    interview_result = candidates[0][1]
    
    for i in range(1, n):
        if interview_result > candidates[i][1]:
            answer += 1
            # 면접 전형에서 가장 높은 등수 갱신
            interview_result = candidates[i][1]
            
    print(answer)