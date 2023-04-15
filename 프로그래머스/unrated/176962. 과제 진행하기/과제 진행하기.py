def to_minute(time):
    # 시간 -> 분 단위로 전환
    hour, minute = map(int, time.split(':'))
    hour_to_min = hour * 60 + minute
    
    return hour_to_min
    
def solution(plans):
    answer = []
    
    # 시간 순 정렬
    plans.sort(key=lambda x:x[1])
        
    stack = []
    # 현재 하고 있는 과목과 다음 대상 과목 비교
    for i in range(len(plans)-1):
        cur_subject, cur_start_time, cur_finish = plans[i]
        cur_start_time = to_minute(cur_start_time)
        cur_finish = int(cur_finish)
        cur_end_time = cur_start_time + cur_finish
        
        nx_subject, nx_start, nx_finish = plans[i+1]
        nx_start = to_minute(nx_start)
        nx_finish = int(nx_finish)
        
        # 현재 과목을 끝내기 전 다음 과제를 해야할 경우
        # 스택에 현재 과목과 남은 시간을 저장
        if cur_end_time > nx_start:
            cur_finish -= nx_start - cur_start_time
            stack.append((cur_subject, cur_finish))
        
        # 현재 과목을 끝내고 다음 과제가 가능할 경우
        else:
            # 현재 과제는 일단 끝났으므로 answer 배열 저장
            answer.append(cur_subject)
            
            # 다음 과제 수행까지 남은 시간을 구함
            remain_time = nx_start - cur_end_time
            
            # 스택에 남은 아직 안끝난 과제
            while remain_time > 0 and stack:
                cur_subject, remain_finish = stack.pop()
                
                # 남은 시간동안 과제를 다 할 수 있는 경우
                if remain_time - remain_finish >= 0:
                    remain_time -= remain_finish
                    answer.append(cur_subject)
                    
                # 남은 시간을 과제를 하는데 다 소모
                else:
                    remain_finish -= remain_time
                    stack.append((cur_subject, remain_finish))
                    break
    
    # 마지막 남은 과제를 답에 추가
    answer.append((plans[-1][0]))
    
    # 스택에 있는 나머지 과목을 모두 끝냄
    while stack:
        subject, _ = stack.pop()
        answer.append(subject)
    
    return answer