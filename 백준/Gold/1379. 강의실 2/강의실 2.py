import sys
import heapq

input = sys.stdin.readline

n = int(input())

# 강의 정보를 저장할 힙
heap = []

# 시작 시간 기준으로 힙에 입력
for _ in range(n):
    idx, s, e = map(int, input().split())
    heapq.heappush(heap, (s, e, idx))

# 처음으로 배정할 강의실 번호 1
classroom_idx = 1

# 최초 시작 강의 배정
classroom = []
s, e, class_idx = heapq.heappop(heap)
classroom.append((e, classroom_idx))

# 강의 번호와 강의실 번호
# 처음 할당된 강의 최초 입력
assigned_classroom = {class_idx : 1}
while heap:
    # (시작, 종료, 강의 번호)
    new_class = heapq.heappop(heap)
    # 강의 번호
    class_idx = new_class[2]
    
    # 새로 배치할 강의 시작 시간과 배치한 수업에서 가장 빠른 종료 시간 비교
    if new_class[0] >= classroom[0][0]:
        # 사용한 강의실에 배치 가능하다면
        end_time, used_classroom_idx = heapq.heappop(classroom)
        heapq.heappush(classroom, (new_class[1], used_classroom_idx))
        assigned_classroom[class_idx] = used_classroom_idx
        
    # 기존 강의가 진행 중이라 새로운 강의실을 할당
    else:
        classroom_idx += 1  # 강의실 번호를 상승
        heapq.heappush(classroom, (new_class[1], classroom_idx))
        assigned_classroom[class_idx] = classroom_idx
        
print(len(classroom))
for i in range(1, n+1):
    print(assigned_classroom[i])
    