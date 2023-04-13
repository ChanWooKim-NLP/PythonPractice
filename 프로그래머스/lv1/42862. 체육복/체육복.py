def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    
    # 제일 마지막 학생은 뒷번호가 없으므로 인덱스 에러 발생
    # 전체 학생 리스트의 길이 1 증가해서 오류 방지
    students = [0] * (n + 2)
    for s_idx in range(1, n+1):
        # 여벌의 체육복은 없지만 도난도 당하지 않은 학생
        if s_idx not in lost and s_idx not in reserve:
            students[s_idx] = 1
    
    # 여분 체육복을 가져온 학생
    # 도난당한 경우도 생각하여 계산
    for s_idx in reserve:
        if s_idx in lost:
            students[s_idx] = 1
        
        else:
            students[s_idx] = 2
    
    # 잃어버린 학생 번호 앞뒤로 하나 빌리기
    # 앞에서 빌릴 수 없으면 뒤에서 빌리기
    for s_idx in lost:
        front, nx = s_idx-1, s_idx+1
        
        if students[front] == 2:
            students[front] -= 1
            students[s_idx] = 1
            
        elif students[nx] == 2:
            students[nx] -= 1
            students[s_idx] = 1
    
    print(students)
    # 체육복이 1개 이상 있으면 참여 가능
    for s_idx in range(1, n+1):
        if students[s_idx] >= 1:
            answer += 1
    
    return answer