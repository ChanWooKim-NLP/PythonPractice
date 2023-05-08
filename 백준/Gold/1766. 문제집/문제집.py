import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def topological_sort(graph):
    # 진입 차수가 0인 정점을 힙에 삽입
    heap = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)
    
    # 위상 정렬 결과 리스트
    sort_result = []
    
    # 힙에서 가장 쉬운 문제부터 꺼내며 위상 정렬 수행
    while heap:
        node = heapq.heappop(heap)
        sort_result.append(node)
        
        for adj in graph[node]:
            indegree[adj] -= 1
            
            if indegree[adj] == 0:
                heapq.heappush(heap, adj)

    return sort_result
    
n, m = map(int, input().split())

# 그래프 딕셔너리와 진입 차수 배열 선언
graph = defaultdict(list)
indegree = [0] * (n+1)

# 간선마다 그래프 정보와 진입 차수
for _ in range(m):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    indegree[b] += 1

sort_result = topological_sort(graph)
print(*sort_result)
