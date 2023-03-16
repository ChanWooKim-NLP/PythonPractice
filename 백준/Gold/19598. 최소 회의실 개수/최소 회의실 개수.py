import heapq
import sys

input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    start, end = map(int, input().split())
    heapq.heappush(heap, (start, end))

# 제일 일찍 시작하는 회의의 종료 시간 집어넣음
conference_room = [heapq.heappop(heap)[1]]
while heap:
    # 새로 시작할 회의의 시작 시간과 종료 시간
    new_start, new_end = heapq.heappop(heap)
    
    # 하나의 회의실을 이어서 사용할 수 있는 회의, 기존 회의의 종료 시간을 pop
    if conference_room[0] <= new_start:
        heapq.heappop(conference_room)
    
    # 이어서 사용 시 기존 회의 pop하고 추가, 아닐 시 pop 과정 없이 회의실 새로 배정
    heapq.heappush(conference_room, new_end)

# 회의실의 길이가 최소 회의실 개수
print(len(conference_room))