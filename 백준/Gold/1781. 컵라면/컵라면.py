import sys
import heapq

input = sys.stdin.readline

n = int(input())

# 과제를 풀 수 있는 최대 데드라인
max_deadline = 0

assignments_list = []
for _ in range(n):
    # 데드라인과 컵라면 수
    d, r = map(int, input().split())
    # 최대 힙으로 삽입
    assignments_list.append((d, r))

    max_deadline = max(max_deadline, d)
    
# 데드라인과 컵라면 수 기준 오름차순 정렬
assignments_list.sort(key=lambda x:(x[0], x[1]))

# 답안
ans = 0

# 특정 기간 동안 풀 수 있는 과제 리스트
candidate_solve = []
for d in range(max_deadline, 0, -1): 
    # 지금 주어진 데드라인 안에 풀 수 있는 과제라면 pop하고 candidate_solve에 추가
    while assignments_list:
        deadline, ramen_cnt = assignments_list[-1]
        
        if deadline < d:
            break
        
        # 최대 힙 구현 위해 음수로 삽입
        # 매 번 정렬하는 것 보다 힙으로 자동 정렬하여 시간 초과 방지
        heapq.heappush(candidate_solve, -ramen_cnt)
        assignments_list.pop()
        
    # 풀 수 있는 과제가 있다면
    if candidate_solve:
        # 최대 힙으로 구현하였기 때문에 차감하여 양수로 전환
        ans -= heapq.heappop(candidate_solve)

print(ans) 