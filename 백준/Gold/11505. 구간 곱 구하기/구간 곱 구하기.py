import sys

input = sys.stdin.readline

def init_tree(node, start, end):
    # 리프 노드에 값을 넣어 줌
    if start == end:
        tree[node] = arr[start]
    
    else:
        mid = (start + end) // 2
        init_tree(node*2, start, mid)
        init_tree(node*2+1, mid+1, end)
        
        # 각 노드의 부모는 해당 구간의 대표값 -> 구간 곱
        tree[node] = tree[node*2] * tree[node*2+1]
        tree[node] %= 1000000007

# start와 end 인덱스 내 left와 right 구간 곱 계산
def query(node, start, end, left, right):
    if right < start or left > end:
        return 1
    
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) * query(node*2+1, mid+1, end, left, right)

def update(node, start, end, index, after_val):
    # 루트 노드인 경우 
    if start == end:
        tree[node] = after_val
        return
    
    mid = (start + end) // 2
    
    # 왼쪽만 업데이트
    if index <= mid:
        update(node*2, start, mid, index, after_val)
    
    # 오른쪽만 업데이트
    else:
        update(node*2+1, mid+1, end, index, after_val)
        
    tree[node] = tree[node*2] * tree[node*2+1]
    tree[node] %= 1000000007

n, m, k = map(int, input().split())

tree = [0] * (4*n)
arr = [0] + [int(input()) for _ in range(n)]

init_tree(1, 1, n)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    
    if a == 1:
        # 변경 전 숫자를 저장하고, 트리의 값을 변경
        arr[b] = c
        update(1, 1, n, b, c)
    
    else:
        product_query = query(1, 1, n, b, c)
        print(product_query % 1000000007)