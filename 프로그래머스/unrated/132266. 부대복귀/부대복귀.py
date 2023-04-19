import heapq
from collections import defaultdict

def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    
    for s, e in roads:
        graph[s].append((e, 1))
        graph[e].append((s, 1))
    
    # destination에서 각 지역 별 거리 리스트
    # 초기 destination 인덱스는 0으로 설정
    visited = [float('inf')] * (n+1)
    visited[destination] = 0
    
    # 거리 / 노드
    heap = [(0, destination)]
    
    # destination에서 다익스트라 시작
    while heap:
        dist, node = heapq.heappop(heap)
        
        # 이미 기록된 거리가 힙에서 꺼낸 노드의 거리보다 작을 경우 계산 X
        if visited[node] < dist:
            continue
            
        for adj_node, n_dist in graph[node]:
            new_dist = n_dist + dist
            
            # 현재 노드를 경유하여 더 짧게 이동할 수 있는 경우
            if new_dist < visited[adj_node]:
                visited[adj_node] = new_dist
                heapq.heappush(heap, (new_dist, adj_node))
                
    # destination에서 각 부대원까지의 위치
    # inf일 경우 복귀할 수 없으므로 -1을 answer에 삽입
    
    answer = []
    for s in sources:
        dist = visited[s]
        
        if dist == float('inf'):
            answer.append(-1)
            
        else:
            answer.append(dist)
    
    return answer