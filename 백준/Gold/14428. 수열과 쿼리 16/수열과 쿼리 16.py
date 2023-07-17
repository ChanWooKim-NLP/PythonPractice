import sys

input = sys.stdin.readline

def init_tree(idx, start, end):
    if start == end:
        tree[idx] = start
        return tree[idx]
    
    mid = (start + end) // 2
    left_idx = init_tree(2*idx, start, mid)
    right_idx = init_tree(2*idx+1, mid+1, end)
    
    if arr[left_idx] <= arr[right_idx]:
        tree[idx] = left_idx
        
    else:
        tree[idx] = right_idx
        
    return tree[idx]

def query(idx, start, end, left, right):
    if left > end or right < start:
        return -1
    
    if left <= start and end <= right:
        return tree[idx]
    
    mid = (start + end) // 2
    left_idx = query(idx*2, start, mid, left, right)
    right_idx = query(idx*2+1, mid+1, end, left, right)
    
    if left_idx == -1:
        return right_idx
    
    elif right_idx == -1:
        return left_idx
    
    else:
        if arr[left_idx] <= arr[right_idx]:
            return left_idx
        
        else:
            return right_idx

def update(node, start, end, change_idx, value):
    if change_idx < start or change_idx > end:
        return
    
    if start == end:
        arr[change_idx] = value
        return
    
    mid = (start + end) // 2
    update(node*2, start, mid, change_idx, value)
    update(node*2+1, mid+1, end, change_idx, value)
    
    if arr[tree[node*2]] <= arr[tree[node*2+1]]:
        tree[node] = tree[node*2]
        
    else:
        tree[node] = tree[node*2+1]
        
n = int(input())

arr = list(map(int, input().split()))
tree = [0] * 4*n

init_tree(1, 0, n-1)

m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    
    if a == 1:
        update(1, 0, n-1, b-1, c)
    
    else:
        idx = query(1, 0, n-1, b-1, c-1)
        print(idx+1)