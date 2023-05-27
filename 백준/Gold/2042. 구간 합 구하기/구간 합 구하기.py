import sys

input = sys.stdin.readline

def init_tree(node_idx, start, end):
    if start == end:
        arr[node_idx] = leaf_nodes[start]
        return arr[node_idx]
        
    else:
        mid = (start + end) // 2
        init_tree(node_idx*2, start, mid)
        init_tree(node_idx*2+1, mid+1, end)
        arr[node_idx] = arr[node_idx*2] + arr[node_idx*2+1]

def query(node_idx, start, end, left, right):
    if right < start or left > end:
        return 0
    
    if left <= start and right >= end:
        return arr[node_idx]
    
    mid = (start + end) // 2
    return query(node_idx*2, start, mid, left, right) + query(node_idx*2+1, mid+1, end, left, right)

def update(node_idx, start, end, index, diff):
    if index < start or index > end:
        return

    arr[node_idx] += diff
    
    if start != end:
        mid = (start + end) // 2
        update(node_idx*2, start, mid, index, diff)
        update(node_idx*2+1, mid+1, end, index, diff)
    
n, m, k = map(int, input().split())

arr = [0] * (4*n)

# 리프 노드에 들어갈 값
leaf_nodes = [0] + [int(input()) for _ in range(n)]

# 트리 생성
init_tree(1, 1, n)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    
    if a == 1:        
        # 차이를 구하여 해당 노드가 관여하는 모든 노드에 업데이트
        diff = c - leaf_nodes[b]
        
        # 리프 노드 업데이트
        leaf_nodes[b] = c
        
        update(1, 1, n, b, diff)
        
    else:
        # b부터 c번 인덱스까지의 구간합을 계산
        sum_query = query(1, 1, n, b, c)
        print(sum_query)
        

