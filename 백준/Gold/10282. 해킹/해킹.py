from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

t = int(input())

# 다익스트라 알고리즘
def dijkstra(start):
    visited = [float('inf')] * (n+1)
    visited[start] = 0
    
    heap = [(0, start)]
    
    while heap:
        dist, com = heapq.heappop(heap)
        
        if visited[com] < dist:
            continue
        
        for adj_com, adj_dist in computers[com]:
            new_dist = dist + adj_dist
            
            if new_dist < visited[adj_com]:
                visited[adj_com] = new_dist
                heapq.heappush(heap, (new_dist, adj_com))
                
    return visited

# 총 감염되는 컴퓨터 수와 전체 감염까지 걸리는 시간
def get_infected_count_and_time(visited):
    infected_count = 0
    infected_time = 0
    
    for idx in range(1, len(visited)):
        if visited[idx] != float('inf'):
            infected_count += 1
            infected_time = max(infected_time, visited[idx])

    return infected_count, infected_time
    
for _ in range(t):
    n, d, c = map(int, input().split())
    
    computers = defaultdict(list)
    
    for _ in range(d):
        a, b, s = map(int, input().split())
        
        computers[b].append((a, s))
    
    # 각 테스트케이스 별 감염 시간 배열
    visited = dijkstra(c)
    infected_count, infected_time = get_infected_count_and_time(visited)
    
    print(infected_count, infected_time)