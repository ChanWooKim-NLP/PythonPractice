def solution(d, budget):
    answer = 0
    d.sort()
    
    for value in d:
        budget -= value
        if budget < 0:
            break
        answer += 1

    return answer