def find(x):
    if parents[x] == x:
        return x
    
    # 노드를 따라가며 부모 노드를 찾고
    # 최종적으로 등장하는 부모(루트)를 기록해야 함
    p = find(parents[x])
    parents[x] = p
    return parents[x]

def union(x, y):
    parent_x = find(x)
    parent_y = find(y)
    
    if parent_x > parent_y:
        parents[parent_x] = parent_y
        
    else:
        parents[parent_y] = parent_x
        
    return

n = int(input())
m = int(input())

parents = [i for i in range(n)]

for i in range(n):
    graph = list(map(int, input().split()))
    
    for j in range(n):
        if graph[j] == 1:
            union(i, j)

plan = list(map(int, input().split()))

# 여행 계획이 가능하면 True 유지
result = True

# 시작
start = parents[plan[0] - 1]
for i in range(1, m):
    # 분리된 도시라 여행 계획에 세울 수 없는 경우
    if parents[plan[i] - 1] != start:
        result = False
        break
        
if result:
    print('YES')
    
else:
    print('NO')