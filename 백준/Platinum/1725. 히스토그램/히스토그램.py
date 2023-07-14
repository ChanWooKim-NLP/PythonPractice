import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)

def init(idx, start, end):
    if start == end:
        tree[idx] = start
        return tree[idx]
    
    mid = (start + end) // 2
    left_idx = init(idx*2, start, mid)
    right_idx = init(idx*2+1, mid+1, end)
    
    if array[left_idx] < array[right_idx]:
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
        if array[left_idx] < array[right_idx]:
            return left_idx
        
        else:
            return right_idx
        
def calculate_area(start, end):
    if start > end:
        return 0
    
    idx = query(1, 0, n-1, start, end)
    area = array[idx] * (end-start+1)
    
    left_area = calculate_area(start, idx-1)
    right_area = calculate_area(idx+1, end)
    
    return max(area, left_area, right_area)

n = int(input())

array = [int(input()) for _ in range(n)]
tree = [0] * 4*n

init(1, 0, n-1)

answer = calculate_area(0, n-1)
print(answer)
