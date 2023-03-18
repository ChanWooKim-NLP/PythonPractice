import sys

input = sys.stdin.readline

n = int(input())

cur_tab = list(map(int, input().split()))
right_tab = list(map(int, input().split()))

stack = [
    b-a for a, b in zip(cur_tab, right_tab)
]

ans = 0
while stack:
    # 스택의 제일 마지막 값
    top = stack.pop()
    
    temp_arr = [top]
    
    # 마지막 원소가 0일 시 스택에서 제외
    if top == 0:
        continue
    
    # 수정해야 할 횟수, top이 음수면 제일 큰 값 / 양수면 제일 작은 값으로 갱신
    # temp_arr에 일관적으로 더하거나 빼준 후 다시 stack에 push함
    indent_cnt = top
    
    # temp : 현재 스택 상태 top, 이전에 꺼낸 top과 변수가 같으면 temp_arr에 저장
    while stack and stack[-1] * top > 0:
        temp = stack.pop()
        temp_arr.append(temp)
        
        if top < 0:
            indent_cnt = max(indent_cnt, temp)
            
        else:
            indent_cnt = min(indent_cnt, temp)
        
    # 같은 부호를 가진 값을 저장한 배열 길이만큼 pop -> ident_cnt와 연산 -> stack에 push
    for _ in range(len(temp_arr)):
        after_correction_cnt = temp_arr.pop() - indent_cnt
        stack.append(after_correction_cnt)
    
    ans += abs(indent_cnt)

print(ans)