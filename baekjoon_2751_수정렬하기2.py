import sys

n = int(sys.stdin.readline())
b = []

for i in range(n):  # 정렬되지 않은 인풋을 만듬
    List = int(sys.stdin.readline())
    b.append(List)
    
def merge_sort(unsorted): # 머지 소트의 기본 개념은 리스트 길이가 1이 될 때 까지 잘게 쪼개는 것
    if len(unsorted) <= 1: # 재귀함수의 탈출구
        return unsorted
    
    a = len(unsorted) // 2 # 리스트 길이의 평균값을 정수형으로 전환
    unsorted_left = unsorted[:a] # a 미만의 인덱스까지를 복사
    unsorted_right = unsorted[a:] # a 이상의 인덱스까지를 복사
    
    left = merge_sort(unsorted_left) # 재귀함수를 이용하여 인덱스 길이가 1이 되면 반환
    right = merge_sort(unsorted_right)
    return merge(left, right)

def merge(left, right):
    result = []  #합병 할 리스트 생성
    while len(left) > 0 or len(right) > 0: # 쪼갠 리스트가 존재할 시 값 대조
        if len(left) > 0 and len(right) > 0: # left와 right 변수에 값이 존재할 시
            if left[0] <= right[0]: # left를 기준으로 이 값이 더 작을 시 결과값에 정렬
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        
        elif len(left) > 0: # 인풋 리스트 길이가 홀수여서 left가 하나 남을 시
            result.append(left[0])
            left = left[1:]
            
        elif len(right) > 0: #right가 하나 남을 시
            result.append(right[0])
            right = right[1:]
            
    return result

for i in merge_sort(b):
    print(int(i))
