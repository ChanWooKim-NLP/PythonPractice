import sys
from collections import defaultdict, deque

def topological_sort(graph: defaultdict, cost: list, indegree: list):
    dp = [0] * (n+1)
    
    queue = deque()
    
    # dp 초기값 설정
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = cost[i]
    
    while queue:
        node = queue.popleft()
        
        for adj in graph[node]:
            indegree[adj] -= 1
            
            if dp[adj] < dp[node] + cost[adj]:
                dp[adj] = dp[node] + cost[adj]
                
            if indegree[adj] == 0:
                queue.append(adj)
    
    return dp

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    graph = defaultdict(list)
    
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    
    indegree = [0] * (n+1)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    w = int(input())
    
    dp = topological_sort(graph, cost, indegree)
    print(dp[w])