import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    
    graph[a].append((b, c))
    graph[b].append((a, c))
    
def dijkstra(start):
    heap = [(0, start, [start])]
    
    path_dict = defaultdict(list)
    
    dist_arr = [float('inf')] * (n+1)
    dist_arr[start] = 0
    
    while heap:
        dist, node, path = heapq.heappop(heap)
        
        if dist > dist_arr[node]:
            continue
        
        for adj_node, adj_dist in graph[node]:
            new_dist = dist + adj_dist
            
            if new_dist < dist_arr[adj_node]:
                dist_arr[adj_node] = new_dist
                new_path = path + [adj_node]
                
                path_dict[adj_node] = new_path
                heapq.heappush(heap, (new_dist, adj_node, new_path))
                
    return path_dict

ans_arr = [
    ['-'] * (n+1)
    for _ in range(n+1)
]

for idx in range(1, n+1):
    ans_arr[idx][idx] = '-'
    
    path_dict = dijkstra(idx)
    for node_idx in path_dict.keys():
        path = path_dict[node_idx]
        ans_arr[idx][node_idx] = path[1]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(ans_arr[i][j], end=' ')
    print()