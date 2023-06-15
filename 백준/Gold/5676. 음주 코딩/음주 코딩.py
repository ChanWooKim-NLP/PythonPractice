import sys

input = sys.stdin.readline

def init_tree(node, start, end):
    # 리프 노드에 값을 넣어 줌
    if start == end:
        tree[node] = arr[start] // max(abs(arr[start]), 1)
    
    else:
        mid = (start + end) // 2
        init_tree(node*2, start, mid)
        init_tree(node*2+1, mid+1, end)
        
        # 각 노드의 부모는 해당 구간의 대표값 -> 구간 곱
        tree[node] = tree[node*2] * tree[node*2+1]

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

tree = [0] * 4000000
while True:
    try:
        n, k = map(int, input().split())
        arr = [0] + list(map(int, input().split()))
        init_tree(1, 1, n)
        
        query_result = ''
        for _ in range(k):
            command, i, v = input().split()
            i = int(i); v = int(v)
            
            # 변경 명령
            if command == 'C':
                v //= max(abs(v), 1)
                update(1, 1, n, i, v)
            
            else:
                result = query(1, 1, n, i, v)
                if result < 0:
                    query_result += '-'
                
                elif result > 0:
                    query_result += '+'
                    
                else:
                    query_result += '0'
        
        print(query_result)

    except Exception as e:
        break