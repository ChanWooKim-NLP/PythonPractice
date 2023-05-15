import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

def dijkstra(graph, m):
    distance_arr = [float('inf')] * m
    distance_arr[0] = 0
    
    heap = [(0, 0, [0])]
    
    path_dict = defaultdict(list)
    path_dict[0].append(0)
    
    while heap:
        dist, node, path = heapq.heappop(heap)
        
        if dist > distance_arr[node]:
            continue
        
        for adj_node, adj_dist in graph[node]:
            new_dist = dist + adj_dist
            new_path = path + [adj_node]
            
            if new_dist < distance_arr[adj_node]:
                distance_arr[adj_node] = new_dist
                path_dict[adj_node] = new_path
                heapq.heappush(heap, (new_dist, adj_node, new_path))

    # 최고위원까지 도달할 수 있다면 경로 리스트 반환
    if distance_arr[m-1] != float('inf'):
        return path_dict[m-1]

    # 만날 수 없다면 -1만 담긴 리스트 반환
    else:
        return [-1]

idx = 1
for _ in range(t):
    n, m = map(int, input().split())
    
    graph = defaultdict(list)
    for _ in range(n):
        x, y, z = map(int, input().split())
        graph[x].append((y, z))
        graph[y].append((x, z))
    
    # 최고위원에게 도달할 수 있는 최소 친밀도를 이루는 경로
    path_to_nth = dijkstra(graph, m)
    
    path = list(map(str, path_to_nth))
    path = ' '.join(path)
    print(f'Case #{idx}: {path}')
    idx += 1