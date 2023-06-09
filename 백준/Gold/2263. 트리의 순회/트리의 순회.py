import sys

sys.setrecursionlimit(1000001)
input = sys.stdin.readline

n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

index_dict = {}
for i in range(n):
    index_dict[inorder[i]] = i

def make_preorder(inorder, postorder, in_start, in_end, p_start, p_end):
    if in_start > in_end or p_start > p_end:
        return []
    
    root = postorder[p_end]
    root_idx = index_dict[root]
    
    print(root, end=' ')
    left_size = root_idx - in_start
    
    left_preorder = make_preorder(inorder, postorder, in_start, root_idx-1, p_start, p_start+left_size-1)
    right_preorder = make_preorder(inorder, postorder, root_idx+1, in_end, p_start+left_size, p_end-1)
    
make_preorder(inorder, postorder, 0, n-1, 0, n-1)
