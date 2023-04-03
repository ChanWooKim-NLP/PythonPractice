import sys
from collections import deque

input = sys.stdin.readline

def bfs(target_idx):
    # BFS에서 사용하는 내부 함수 -> 해당 방으로 들어갈 수 있는지 확인
    def can_enter(room_info):
        nonlocal cur_gold
        
        in_room = room_info[0]
        gold = int(room_info[1])
        
        # 방의 종류 별로 gold 갱신
        if in_room == 'L':
            cur_gold = max(cur_gold, gold)
            return True
            
        elif in_room == 'T':
            if cur_gold >= gold:
                cur_gold -= gold
                return True
            
            else:
                return False
        
        # 빈 방이면 통과    
        elif in_room == 'E':
            return True
    
    # 최초로 들어가는 방은 첫 번째 인덱스 방
    queue = deque([1])
    cur_gold = 0
    
    visited = [0] * (n+1)
    
    while queue:
        dq_idx = queue.popleft()
        dq_idx = int(dq_idx)
        next_room = maze[dq_idx]
        
        # queue에는 탐색 후보 방 -> can_enter 를 통해 들어갈 수 있는지 확인
        if can_enter(next_room) and not visited[dq_idx]:
            # 들어갈 수 있는 방 + 목적지 -> True
            if dq_idx == target_idx:
                return True
            
            visited[dq_idx] = 1 
            # 들어갈 수 있다면 queue에 extend
            queue.extend(next_room[2:])        
    
    return False

while True:
    n = int(input())
    if n == 0:
        break
    
    # 인덱스를 맞추기 위해 n+1 크기 배열
    maze = [[]] * (n+1)
    
    # 미로 정보
    for idx in range(1, n+1):
        info = input().split()
        maze[idx] = info[:-1]
    
    # 끝 번호까지 갈 수 있으면 True
    result = bfs(n)
    
    if result:
        print('Yes')
        
    else:
        print('No')
        
