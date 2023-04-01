def str_to_length(string: str):
    if string.islower():
        return ord(string) - 96

    else:
        return ord(string) - 38

n = int(input())

# 각 컴퓨터와 연결된 루트 노드
parents = [i for i in range(n)]

# 정점 및 간선 가중치
graph = []

# 다솜이가 가진 랜선 길이 합
total_length = 0
for i in range(n):
    lan_list = input()
        
    for j in range(n):
        if lan_list[j] != '0':
            all_zero = False
            # 문자열 -> 길이 치환
            length = str_to_length(lan_list[j])
            
            # 그래프에 간선 연결과 가중치 튜플 삽입
            graph.append((i, j, length))
            # 전체 랜선 길이 업데이트
            total_length += length


def find(x):
    # 루트 확인
    if parents[x] == x:
        return x
    
    # 경로를 압축하여 연결된 그래프가 같은 루트를 가리키도록 설정
    root = find(parents[x])
    parents[x] = root
    return parents[x]

# 연결이 안된 경우 두 정점 연결, 부모 노드 정보 업데이트
def union(x, y):
    parent_x = find(x)
    parent_y = find(y)
    
    if parent_x > parent_y:
        parents[parent_x] = parent_y
        
    else:
        parents[parent_y] = parent_x

# 간선 가중치 기준 정렬
graph.sort(key=lambda x: x[2])

# 답안
ans = 0

# 연결한 랜선, 가진 랜선 길이에서 빼 줌
connected = 0

# 연결 수행
for edge in graph:
    x, y, weight = edge
    
    if find(x) != find(y):
        union(x, y)
        connected += weight

# 전체 부모 노드 업데이트
for idx in range(n):
    parents[idx] = find(parents[idx])

ans = total_length - connected

# 모든 컴퓨터가 연결되지 않은 경우 -1 출력
for i in range(n-1):
    if parents[i] != parents[i+1]:
        ans = -1
        break
               
print(ans)
