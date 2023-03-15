import sys

input = sys.stdin.readline

# 접근 방법
# 현재 day에서 최대 점수를 얻을 수 있는 과제 탐색
# day는 역순으로 시작
n = int(input())

assign_list = []
for _ in range(n):
    d, w = map(int, input().split())
    assign_list.append((d, w))

# 날짜와 점수 순으로 오름차순 정렬
assign_list.sort(key=lambda x: (x[0], x[1]))

answer = 0

# 현재 시점에서 수행 가능한 과제
candidate_assigns = []

# 마지막 day에서부터 얻을 수 있는 점수 탐색
for d in range(n, 0, -1):
    
    # pop하기 전 수행 가능한 과제와 점수 확인 
    while assign_list:
        deadline, score = assign_list[-1]
        
        # 제출 기간이 넘으면 반복문 종료
        if deadline < d:
            break
        
        # 수행 가능 리스트에 점수 추가
        candidate_assigns.append(score)
        
        # 같은 과제를 다시 선정하는 것을 막기 위해 후보에 넣었으면 pop
        assign_list.pop()
    
    # 수행 가능한 과제가 있으면 점수 순으로 정렬하고 제일 큰 값을 출력
    if candidate_assigns:
        candidate_assigns.sort()
        answer += candidate_assigns.pop()
            
print(answer)