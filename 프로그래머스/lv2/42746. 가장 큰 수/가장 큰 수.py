def solution(numbers):
    # edge case : 모든 수가 0일 때
    all_zeros = True
    for i in numbers:
        if i != 0:
            all_zeros = False
            break
    
    if all_zeros:
        return '0'
    
    # 모든 값을 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 모든 문자열의 길이를 3 이상으로 만들어 정렬 진행
    # 1000 이하이므로 4-1, 3자리로 만들어 문자열 기준으로 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
        
    return answer