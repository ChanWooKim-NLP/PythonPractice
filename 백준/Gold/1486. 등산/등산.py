import heapq

n, m, t, d = map(int, input().split())

arr = [
    [0] * m
    for _ in range(n)
]

for i in range(n):
    string = input()
    
    for j in range(m):
        val = 0
        if string[j].isupper():
            val = ord(string[j]) - 65
            
        else:
            val = ord(string[j]) - 71
        
        arr[i][j] = val

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 다익스트라
# 호텔에서 올라갈 수 있는 모든 시간을 구한 후
# 도달 가능한 곳에서 다시 호텔까지 내려오는 시간을 구함
# 두 시간의 합이 d를 넘지 않는다면 최대로 올라갈 수 있는 높이를 구할 수 있음
def dijkstra(x, y):
    visited = [
        [float('inf')] * m
        for _ in range(n)
    ]
    visited[x][y] = 0
    
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
    
    heap = [(0, x, y)]
    
    while heap:
        time, x, y = heapq.heappop(heap)
        
        if visited[x][y] < time:
            continue
        
        cur_height = arr[x][y]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if not in_range(nx, ny):
                continue
            
            nx_height = arr[nx][ny]
            
            if abs(nx_height - cur_height) > t:
                continue
            
            if cur_height >= nx_height:
                nx_time = time + 1
                
            else:
                nx_time = time + (cur_height-nx_height)**2
                
            if visited[nx][ny] > nx_time:
                visited[nx][ny] = nx_time
                heapq.heappush(heap, (nx_time, nx, ny))
                
    return visited


# 호텔에서 출발하여 각 좌표까지 도달 시간
visited_from_hotel = dijkstra(0, 0)

can_visit_heap = []

for i in range(n):
    for j in range(m):
        if visited_from_hotel[i][j] <= d:
            heapq.heappush(can_visit_heap, (-arr[i][j], i, j))

while can_visit_heap:
    max_height, x, y = heapq.heappop(can_visit_heap)
    
    visited_to_hotel = dijkstra(x, y)
    
    if visited_from_hotel[x][y] + visited_to_hotel[0][0] <= d:
        # 최대 힙으로 넣었기 때문에 음수를 곱하여 양수로 출력
        print(-max_height)
        break
        