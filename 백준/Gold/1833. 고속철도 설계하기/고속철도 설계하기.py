import sys

input = sys.stdin.readline

n = int(input())

trails = [
    list(map(int, input().split()))
    for _ in range(n)
]

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

costs = []
total_cost = 0  # 전체 비용

parents = [i for i in range(n)]

# 함정 : 설치되지 않는 경로의 길이는 입력값에서 가장 최댓값으로 표현
# 1000은 모든 테스트케이스에서 제외되는 수가 아님
for i in range(n):
    for j in range(i+1, n):
        if trails[i][j] < 0:
            total_cost += abs(trails[i][j])
            union(i, j)
            
        else:
            costs.append((i, j, trails[i][j]))
            
costs.sort(key=lambda x: x[-1])

# 새로 설치하는 고속철도 개수
m = 0

# 고속도로가 새로 설치된 두 도시 번호의 리스트
new_trails_list = []
for i, j, cost in costs:
    if find(i) != find(j):
        union(i, j)
        
        # 전체 비용
        total_cost += cost
        m += 1
        # 1부터 인덱스가 시작하도록 1을 더해줌
        new_trails_list.append((i+1, j+1))
        
print(total_cost, m)
for i, j in new_trails_list:
    print(i, j)