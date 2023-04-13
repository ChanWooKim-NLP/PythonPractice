from collections import defaultdict
import heapq


def solution(N, road, K):
    answer = 0

    graph = defaultdict(list)
    for a, b, w in road:
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    visited = [float('inf')] * (N+1)
    visited[1] = 0
    
    heap = [(1, 0)]
    
    while heap:
        n, dist = heapq.heappop(heap)
        
        if visited[n] < dist:
            continue
            
        for adj_n, adj_w in graph[n]:
            new_dist = dist + adj_w
            
            if visited[adj_n] > new_dist:
                visited[adj_n] = new_dist
                heapq.heappush(heap, (adj_n, new_dist))
                
    for idx in range(1, N+1):
        if visited[idx] <= K:
            answer += 1
    
    return answer