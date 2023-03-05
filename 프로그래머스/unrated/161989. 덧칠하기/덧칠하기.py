def solution(n, m, section):        
    answer = 0
        
    paint_start = section[0] - 1
    
    for s in section:
        # 구간을 넘기면 새로 롤러칠 진행
        if paint_start < s:
            paint_start = s + m - 1
            answer += 1
        
    return answer                                                                                                                                                                                                                                                                            