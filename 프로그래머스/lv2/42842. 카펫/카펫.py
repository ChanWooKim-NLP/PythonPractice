from math import sqrt

def solution(brown, yellow):
    answer = []
    
    total_cnt = brown + yellow
    
    # 3부터 sqrt_cnt까지 세로 길이 늘려가며 조건에 맞는지 확인
    sqrt_cnt = int(sqrt(total_cnt))
    
    for h in range(3, sqrt_cnt + 1):
        # 나머지가 0이 아니라면 사각형이 성립하지 않음
        if total_cnt % h != 0:
            continue
        
        # 세로 길이를 토대로 가로 길이 도출
        v = total_cnt // h
        
        # 갈색 격자의 개수가 입력값이랑 맞는지 확인
        cur_brown_cnt = v*2 + (h-2)*2
        if cur_brown_cnt == brown:
            answer = [v, h]
    
    return answer