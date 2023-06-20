import sys
from collections import defaultdict, deque

input = sys.stdin.readline

graph = defaultdict(list)
n = int(input())

indegree = [0] * (n+1)
times = [0] * (n+1)
for idx in range(1, n+1):
    info = list(map(int, input().split()))
    
    build_time = info[0]
    times[idx] = build_time
    
    # 현재 건물을 짓기 전에 지어야 할 건물과 현재 건물을 방향 그래프로 추가
    for j in range(1, len(info)-1):
        graph[info[j]].append(idx)
        indegree[idx] += 1
        
def topological_sort():
    # 각 건물이 건설 완료될 때 까지 걸리는 총 시간
    dp = [0] * (n+1)
    
    queue = deque()
    
    # 진입 차수가 0인 노드
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = times[i]
    
    while queue:
        cur_build = queue.popleft()
        
        for adj_build in graph[cur_build]:
            indegree[adj_build] -= 1
            
            # 해당 건물을 완전히 짓기 위해선 의존성 있는 다른 건물 건설이 완료되야 함
            # 의존성 관계에 있는 건물 건설 시간 + 해당 건물 빌드 시간이 최대화되는 시간
            if dp[adj_build] < dp[cur_build] + times[adj_build]:
                dp[adj_build] = dp[cur_build] + times[adj_build]

            # 진입 차수가 0이 된다면 큐 삽입
            if indegree[adj_build] == 0:
                queue.append(adj_build)
                
    return dp

dp = topological_sort()
for i in range(1, n+1):
    print(dp[i])