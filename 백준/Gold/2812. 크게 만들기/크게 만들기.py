import sys

input = sys.stdin.readline

n, k = map(int, input().split())

# str로 입력받음
num = input().strip()

# 스택으로 가장 큰 수의 자리수 관리
# 스택의 top과 현재 수를 비교 반복 진행
stack = []

delete_cnt = 0

for i in range(n):
    # 스택이 비거나, 삭제할 개수가 다 차면 진행 X
    while delete_cnt != k and stack:
        # stack의 top보다 현재 위치한 인덱스의 숫자가 더 클 경우 
        # 스택에서 pop하고 삭제 cnt 증가
        #  -> 스택에서 현재 숫자보다 크거나 같은 숫자가 나올 때 까지 pop 반복함
        if stack[-1] < num[i]:
            stack.pop()
            delete_cnt += 1

        # 크거나 같은 경우에만 break로 while문 탈출
        else:
            break
        
    stack.append(num[i])

# n-k까지 출력
print(''.join(stack[:n-k]))

