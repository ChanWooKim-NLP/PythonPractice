import sys

n = int(sys.stdin.readline())
b = []

for i in range(n):
    List = int(sys.stdin.readline())
    b.append(List)
    
def merge_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    
    a = len(unsorted) // 2
    unsorted_left = unsorted[:a]
    unsorted_right = unsorted[a:]
    
    left = merge_sort(unsorted_left)
    right = merge_sort(unsorted_right)
    return merge(left, right)

def merge(left, right):
    result = []  #합병 할 리스트 생성
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
            
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
            
    return result

for i in merge_sort(b):
    print(int(i))
