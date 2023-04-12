def solution(A,B):
    answer = 0

    # A를 오름차순, B를 내림차순 정렬
    # 가장 큰 수와 가장 작은 수를 곱하여 도해주면 최소값
    A.sort()
    B.sort(reverse=True)
    
    for i, j in zip(A, B):
        answer += i*j

    return answer