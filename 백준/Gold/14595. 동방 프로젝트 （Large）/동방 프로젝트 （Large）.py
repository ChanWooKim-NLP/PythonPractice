import sys

input = sys.stdin.readline

# 겹치는 선분 구간을 구하고, 방을 하나로 합치기 위한 union-find
def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    px, py = find(x), find(y)
    
    if px > py:
        parents[px] = py
        
    else:
        parents[py] = px

n = int(input())
m = int(input())

# 빅-종빈맨이 벽을 부수는 동방 행동 리스트
# 선분으로 취급
points = [
    list(map(int, input().split()))
    for _ in range(m)
]

# 충분히 큰 값을 좌표
# 입력값 중 마지막 선분의 좌표도 겹치는 선분 리스트에 추가할 수 있도록 설정
points.append([1e9, 1e9])

# 시작 / 끝 점 기준으로 정렬
points.sort()

# 초기 선분 시작점과 끝 점
start_point = points[0][0]
end_point = points[0][1]

overlap_points_list = []
for x, y in points:
    # 겹치지 않는다면 현재까지 겹치는 선분 구간을 구하고
    # 새로운 선분 시작점을 정의함
    if x > end_point:
        overlap_points_list.append((start_point, end_point))
        start_point = x
    
    end_point = max(end_point, y)    

# union-find 위한 각 방의 부모 방
parents = [i for i in range(n+1)]

for start, end in overlap_points_list:
    for room_idx in range(start, end+1):
        if find(start) != find(room_idx):
            union(start, room_idx)

# 합쳐진 방의 개수는 union-find 후 parents의 고유 원소의 개수
# parents에서 0번 인덱스는 인덱스를 1부터 시작하기 위해 존재하는 더미 인덱스 -> -1 차감
room_cnt = len(set(parents))
room_cnt -= 1

print(room_cnt)
