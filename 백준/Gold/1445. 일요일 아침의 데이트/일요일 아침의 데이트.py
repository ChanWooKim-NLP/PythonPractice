from collections import deque
import heapq

n, m = map(int, input().split())

forest = [
    list(input())
    for _ in range(n)
]

# 비용 그래프
# 0 인덱스 : 해당 구간까지 쓰레기를 거쳐가는 횟수
# 1 인덱스 : 해당 구간까지 쓰레기 주변을 거쳐가는 횟수
dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 숲에서 시작점과 도착지, 쓰레기와 그 주변 좌표에 거리를 기록
start, end = (-1, -1), (-1, -1)
for i in range(n):
    for j in range(m):
        if forest[i][j] == 'S':
            start = (i, j)
        
        elif forest[i][j] == 'F':
            end = (i, j)
        
        # 쓰레기와 그 주변 좌표에 거리를 기록
        elif forest[i][j] == 'g':
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                
                # 쓰레기 바로 옆 쓰레기와 출발/도착지가 있는 경우는 제외
                if in_range(nx, ny) and forest[nx][ny] not in 'SFg':
                    forest[nx][ny] = '#'

visited = [
    [0] * m
    for _ in range(n)
]


def bfs(x, y):    
    # 좌표와 초기 거리, 쓰레기 주변과 쓰레기를 거친 횟수
    queue = []
    heapq.heappush(queue, (0, 0, x, y))
    
    visited[x][y] = 1
    while queue:
        # 거쳐간 쓰레기 / 쓰레기 주변 칸 개수
        g, sur_g, x, y = heapq.heappop(queue)
        
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny) and not visited[nx][ny]:
                # 방문 확인
                visited[nx][ny] = 1
                
                if forest[nx][ny] == 'F':
                    return g, sur_g
                
                # 다음 위치가 쓰레기
                if forest[nx][ny] == 'g':
                    heapq.heappush(queue, (g+1, sur_g, nx, ny))
                
                # 쓰레기 주변
                elif forest[nx][ny] == '#':
                    heapq.heappush(queue, (g, sur_g+1, nx, ny))

                # 아무것도 없는 경우
                elif forest[nx][ny] == '.':
                    heapq.heappush(queue, (g, sur_g, nx, ny))

    # ide에서 나타나는 오류를 방지하기 위한 더미 코드
    # 아래가 반환되는 경우는 없음
    return -1, -1

result = bfs(start[0], start[1])
print(result[0], result[1])