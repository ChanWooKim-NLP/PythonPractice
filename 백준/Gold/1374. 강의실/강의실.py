import heapq
import sys
from pprint import pprint

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    idx, start, end = map(int, input().split())
    heapq.heappush(heap, [start, end, idx])

# 강의실 목록, 종료 시간만 기록
lecture_room = []

# 첫 강의의 종료 시간
_, end, _ = heapq.heappop(heap)
heapq.heappush(lecture_room, end)

while heap:
    new_lecture = heapq.heappop(heap)
    start_time_new_lecture = new_lecture[0]
    end_time_new_lecture = new_lecture[1]
    # 가장 빨리 끝나는 강좌의 종료 시간
    end_time = lecture_room[0]
    
    # 강의실에 집어넣은 강의가 끝나는 시간과 집어넣을 강의의 시작 시간 비교
    # 기존 강의실에 집어넣을 수 있다면 강의실 heap에서 가장 일찍 끝나는 강의 pop
    if end_time <= start_time_new_lecture:
        heapq.heappop(lecture_room)
    
    # 새 강의의 종료 시간을 heap에 삽입
    heapq.heappush(lecture_room, end_time_new_lecture)
    
print(len(lecture_room))