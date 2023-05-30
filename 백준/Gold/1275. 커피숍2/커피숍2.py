import sys

input = sys.stdin.readline

def init_tree(node, start, end):
    if start == end:
        tree[node] = arr[start]
    
    else:
        mid = (start + end) // 2
        init_tree(node*2, start, mid)
        init_tree(node*2+1, mid+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def query(node, start, end, left, right):
    if right < start or left > end:
        return 0
    
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    
    tree[node] += diff
    
    if start != end:
        mid = (start + end) // 2
        update(node*2, start, mid, index, diff)
        update(node*2+1, mid+1, end, index, diff)
                
n, q = map(int, input().split())

arr = [0] + list(map(int, input().split()))
tree = [0] * (4*n)

init_tree(1, 1, n)

for _ in range(q):
    x, y, a, b = map(int, input().split())
    
    # x부터 y번째 인덱스 합을 구함
    # x보다 y가 크다면 값을 바꿈
    if x > y:
        x, y = y, x
        
    tree_sum = query(1, 1, n, x, y)
    print(tree_sum)
    
    # a번째 인덱스 수를 b로 바꾼다
    # 바꾼 수와 원래 수의 차이를 구한 후 트리에 반영
    diff = b - arr[a]
    arr[a] = b
    
    update(1, 1, n, a, diff)
    
    