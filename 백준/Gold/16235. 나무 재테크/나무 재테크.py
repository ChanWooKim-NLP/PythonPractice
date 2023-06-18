import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

ground = defaultdict(deque)

nutrition = [
    [5] * n
    for _ in range(n)
]

plus_nutrition = [
    list(map(int, input().split()))
    for _ in range(n)
]

for _ in range(m):
    x, y, z = map(int, input().split())
    # 인덱스를 맞추기 위해 1씩 차감
    x -= 1; y -= 1
    
    # 나무 나이 삽입
    ground[(x, y)].append(z)
    
# 봄 -> 나무가 자신의 위치에서 나이만큼 양분을 먹고 나이 1 증가
# 그것이 안된다면 죽고, 여름에 해당 위치에 양분으로 남음
def spring_and_summer():    
    # key : 나무가 심어진 좌표 튜플
    for key in list(ground.keys()):
        x, y = key
        # 해당 좌표에 새로 기록할 나무 나이 정보
        temp_deque = deque()
        
        # 현재 좌표에서 죽은 나무
        dead_tree = 0
        
        # 나이가 어린 나무부터 양분을 먹음
        for tree_age in ground[key]:
            # 양분을 먹을 수 있는 경우 나이만큼 먹고 임시 힙에 삽입
            if nutrition[x][y] >= tree_age:
                temp_deque.append(tree_age+1) # 임시 큐에 저장
                nutrition[x][y] -= tree_age
            
            # 먹을 수 없다면 죽음
            else:
                dead_tree += tree_age // 2

        # 새로 기록한 나무 나이 저장
        ground[key] = temp_deque
        
        # 해당 위치에서 죽은 나무로 양분 추가
        nutrition[x][y] += dead_tree


# 가을에는 나이가 5배수인 나무가 주변 8칸으로 번식
def autumn_and_winter():
    # 나무가 번식하는 주변 위치
    dxs = [-1, -1, -1, 0, 0, 1, 1, 1]
    dys = [-1, 0, 1, -1, 1, -1, 0, 1]
        
    for key in list(ground.keys()):
        x, y = key
        for tree_age in ground[key]:
            if tree_age % 5 != 0:
                continue
            
            # 주변 8칸으로 나이가 1인 나무 번식
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                
                # 땅을 벗어나지 않는다면 해당 칸으로 번식
                if 0 <= nx < n and 0 <= ny < n:
                    ground[(nx, ny)].appendleft(1)
    
    # 겨울에는 로봇이 땅을 돌아다니며 양분을 추가함
    for x in range(n):
        for y in range(n):
            nutrition[x][y] += plus_nutrition[x][y]
        
            
# k년 동안 계절 사이클을 반복 후 전체 나무의 개수를 구한다.
for _ in range(k):
    spring_and_summer()
    autumn_and_winter()

answer = 0
for key in list(ground.keys()):
    answer += len(ground[key])
        
print(answer)