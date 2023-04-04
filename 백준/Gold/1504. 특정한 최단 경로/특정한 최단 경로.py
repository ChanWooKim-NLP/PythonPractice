import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, e = map(int, input().split())

graph = defaultdict(list)

for _ in range(e):
    a, b, c = map(int, input().split())
    
    graph[a].append((b, c))
    graph[b].append((a, c))
    
u, v = map(int, input().split())

# 시작 노드와 목적지 노드까지 최단 거리를 구하는 다익스트라 함수
def dijkstra(start_node, target_node):
    # 거리 배열 초기화
    dist = [float('inf')] * (n+1)
    dist[start_node] = 0
    
    # 인접한 노드 간 최단 거리를 구하기 위한 힙
    heap = []
    heapq.heappush(heap, (start_node, 0))
    
    while heap:
        # 출발지에서 해당 노드까지의 거리
        node, weight = heapq.heappop(heap)
        
        # 이미 기록된 거리보다 더 크면 다음 노드로 넘어감
        if dist[node] < weight:
            continue
        
        # 인접한 노드로 갈 수 있는 거리 계산 후 갱신
        for adj_node, adj_weight in graph[node]:
            new_dist = weight + adj_weight
            
            if new_dist < dist[adj_node]:
                dist[adj_node] = new_dist
                heapq.heappush(heap, (adj_node, new_dist))

    # 목적지 노드까지의 최단거리, inf라면 경로가 없는 것
    return dist[target_node]

# 1->u, u->v, v->n 순으로 최단 거리를 구한 후 더함
dist_first_to_uth_node = dijkstra(1, u)
dist_uth_to_vth_node = dijkstra(u, v)
dist_vth_to_nth_node = dijkstra(v, n)

dist_1 = dist_first_to_uth_node + dist_uth_to_vth_node + dist_vth_to_nth_node

# 1->v, v->u, u->n
dist_first_to_vth_node = dijkstra(1, v)
dist_vth_to_uth_node = dijkstra(v, u)
dist_uth_to_nth_node = dijkstra(u, n)

dist_2 = dist_first_to_vth_node + dist_vth_to_uth_node + dist_uth_to_nth_node
 
# 세 거리를 더한 결과가 무한대라면 경로가 없음
if dist_1 != float('inf') and dist_2 != float('inf'):
    print(min(dist_1, dist_2))
    
else:
    print(-1)