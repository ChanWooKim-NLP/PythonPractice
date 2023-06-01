import sys

input = sys.stdin.readline

def init_tree(node, start, end):
    if start == end:
        tree_min[node] = arr[start]
        tree_max[node] = arr[start]
        
    else:
        mid = (start + end) // 2
        init_tree(node*2, start, mid)
        init_tree(node*2+1, mid+1, end)
        tree_min[node] = min(tree_min[node*2], tree_min[node*2+1])
        tree_max[node] = max(tree_max[node*2], tree_max[node*2+1])
        
def query_min(node, start, end, left, right):
    if right < start or left > end:
        return float('inf')
    
    if left <= start and right >= end:
        return tree_min[node]
    
    mid = (start + end) // 2
    return min(query_min(node*2, start, mid, left, right), query_min(node*2+1, mid+1, end, left, right))

def query_max(node, start, end, left, right):
    if right < start or left > end:
        return float('-inf')
    
    if left <= start and right >= end:
        return tree_max[node]
    
    mid = (start + end) // 2
    return max(query_max(node*2, start, mid, left, right), query_max(node*2+1, mid+1, end, left, right))


n, m = map(int, input().split())

arr = [0] * (n+1)
tree_min = [0] * (4*n)
tree_max = [0] * (4*n)

for idx in range(1, n+1):
    val = int(input())
    arr[idx] = val

init_tree(1, 1, n)

for _ in range(m):
    a, b = map(int, input().split())
    
    min_val = query_min(1, 1, n, a, b)
    max_val = query_max(1, 1, n, a, b)
    print(min_val, max_val)