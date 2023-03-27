n = int(input())

lecture = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

lecture.sort(key=lambda x: (x[1], x[0]))

# 엣지 케이스 : 강연 요청이 0개일 때
max_day = 0
if n > 0:
    # 강연할 수 있는 최대 일
    max_day = lecture[-1][1]

ans = 0

candidate_lecture = []    
for d in range(max_day, 0, -1):
    # 하루에 한 번 강연 가능    
    while lecture:
        payment, deadline = lecture[-1]
        # d일 이내에 불가능한 강연이라면 탐색 제외
        if deadline < d:
            break
        
        # 강연 가능 목록에 해당 강연의 수당 추가
        # 해당 강연은 원래 목록인 lecture 배열에서 제외
        candidate_lecture.append(payment)
        lecture.pop()

    # 후보 목록 정렬하여 가장 많이 받는 강연의 수당 더해줌
    # 강연을 했으면 그 날에는 더 이상 할 수 없으므로 can_lecture를 False로 설정
    if candidate_lecture:
        candidate_lecture.sort()
        ans += candidate_lecture.pop()
        
print(ans)