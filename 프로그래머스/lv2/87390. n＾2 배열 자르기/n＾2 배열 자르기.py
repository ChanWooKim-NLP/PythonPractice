def solution(n, left, right):
    answer = []
    
    for idx in range(left, right+1):
        # 1차원 배열의 인덱스가 원본 2차원 배열에서 표현되는 행과 열
        i, j = divmod(idx, n)
        
        # 2차원 배열에서 해당 좌표가 의미하는 값
        val = max(i, j) + 1
        answer.append(val)
        
        
    return answer