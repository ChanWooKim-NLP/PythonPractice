import sys

n, c = map(int, sys.stdin.readline().split())

points = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

# 비용 배열
# 메모리 절약을 위해 공간복잡도 O(n)인 1차원 배열 사용
# 모든 정점 간 거리를 저장하는 경우 O(n^2)이므로 메모리 초과 발생
dist = [float('inf')] * n

# x좌표와 y좌표 저장
x = [p[0] for p in points]
y = [p[1] for p in points]

# 시작 노드 번호
node_idx = 0

# 정답
answer = 0

# n-1번 반복 -> mst를 이루기 위한 최소 간선 개수
for _ in range(n - 1):
    # 방문한 노드 처리 위해 -1로 표현
    dist[node_idx] = -1

    # 연결할 수 있는 다른 좌표 탐색
    for j in range(n):
        d = (x[node_idx] - x[j]) ** 2 + (y[node_idx] - y[j]) ** 2
        # 비용이 c 이상이고, 현재 기록된 비용보다 작다면 갱신
        if d >= c and d < dist[j]:
            dist[j] = d

    # 다음으로 살펴볼 노드 인덱스
    node_idx = -1
    # 모든 다른 정점에 대해
    for j in range(n):
        # 아직 방문하지 않았고, 비용이 기록된 경우
        if dist[j] != -1 and dist[j] != float('inf'):
            # 아직 다음 정점을 결정하지 않았거나, 살펴본 j번째 좌표가 현재 노드에서 연결 가능한 최소 비용인 경우
            if node_idx == -1 or dist[node_idx] > dist[j]:
                node_idx = j    # 살펴볼 다음 노드로 갱신

    # 위에서 갱신되지 않았다면 다음으로 이동 가능한 노드가 없으므로 종료
    if node_idx == -1:
        break
    
    # 아니라면 현재 노드와 다음 이동 노드 간 간선 거리를 더해 줌
    answer += dist[node_idx]

# 연결 가능한 노드가 없어 갱신 없이 반복문이 종료된 경우 mst 구성 불가
if node_idx == -1:
    answer = -1

print(answer)