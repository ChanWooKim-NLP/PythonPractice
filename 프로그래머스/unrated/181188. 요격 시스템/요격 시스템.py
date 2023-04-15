import heapq

def solution(targets):
    targets.sort(key=lambda x:(x[1], x[0]))
    
    # 초기 끝점
    # targets의 시작점과 비교하여 한 번에 요격 가능한지 확인
    e = 0
    
    answer = 0
    for t in targets:
        # 끝 점이 겹치면 다시 요격을 해야함
        if t[0] >= e:
            answer += 1
            e = t[1]
            
    return answer