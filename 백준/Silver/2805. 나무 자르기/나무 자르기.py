import sys

input = sys.stdin.readline

n, m = map(int, input().split())

tree_list = list(map(int, input().split()))

min_tree = 0
max_tree = max(tree_list)

def cut_tree(h):
    cnt = 0
    
    for tree in tree_list:
        if tree > h:
            cnt += tree - h
        
    return cnt

while min_tree <= max_tree:
    mid = (min_tree + max_tree) // 2
    
    tree_cnt = cut_tree(mid)
    if tree_cnt < m:
        max_tree = mid - 1
        
    else:
        min_tree = mid + 1
        
print(min_tree- 1)