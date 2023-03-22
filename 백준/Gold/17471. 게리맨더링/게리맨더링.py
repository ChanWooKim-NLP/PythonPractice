import sys
from collections import defaultdict, deque


input = sys.stdin.readline

n = int(input())

graphs = defaultdict(list)

people = list(map(int, input().split()))

for i in range(1, n+1):
    info = list(map(int, input().split()))
    
    for j in range(1, len(info)):
        adj = info[j]
        
        # 인접 노드 그래프에 기록
        graphs[i].append(adj)
        
def backtracking(cnt, start_idx, target_cnt):
    global ans
    if cnt == target_cnt:
        group_1, group_2 = [], []
        
        # 조합한 구와 아닌 구를 각각 배열에 집어 넣음
        for i in range(1, n+1):
            if visited[i]:
                group_1.append(i)
            
            else:
                group_2.append(i)    
        
        result1, result2 = bfs(group_1), bfs(group_2)
        # 두 구로 정확히 나눌 수 있는 상황
        if result1 and result2:
            ans = min(ans, abs(result1-result2))
        
        return
    
    for i in range(start_idx, n+1):
        if not visited[i]:
            visited[i] = 1
            
            # 현재 인덱스에서 새로운 도시 조합 진행
            backtracking(cnt+1, i, target_cnt)
            visited[i] = 0

    return

def bfs(group):
    queue = deque([group[0]])
    
    bfs_visited = [0] * (n+1)
    
    visited_cnt = 0
    total_people = 0
    
    while queue:
        node = queue.popleft()
        
        if not bfs_visited[node]:
            total_people += people[node-1]
            bfs_visited[node] = 1
            visited_cnt += 1
            
        for adj in graphs[node]:
            if adj in group and not bfs_visited[adj]:
                queue.append(adj)
                
    if visited_cnt == len(group):
        return total_people
    
    return
    
ans = float('inf')

for i in range(1, n//2 + 1):
    visited = [0] * (n+1)
    backtracking(0, 1, i)

if ans == float('inf'):
    print(-1)

else:
    print(ans)