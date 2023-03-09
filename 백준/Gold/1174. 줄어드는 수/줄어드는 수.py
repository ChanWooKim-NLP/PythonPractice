# 최근 넣은 수보다 작은 수만 for문을 통해 배열 num에 삽입
# 최대 가능 자리수는 9부터 0까지 10자리
def backtracking(n, cur_digit, target_digit, num=[], end=9):
    global order
    
    # 현재 자리수와 목표하는 자리수가 같다면 순서 증가
    # 입력한 n과 현재 완성한 수의 순서가 같다면 출력
    # 숫자로 배열에 입력하였으므로 str형으로 바꾸어 join
    if cur_digit == target_digit:
        if order == n:
            answer = ''.join(map(str, num))
            print(answer)
        order += 1
        return
    
    
    for idx in range(0, end+1):
        num.append(idx)
        backtracking(n, cur_digit+1, target_digit, num, idx-1)
        num.pop()

n = int(input())
# 줄어드는 수의 최대 개수는 1023개
if n > 1023:
    print(-1)

else:
    order = 1
    for target_digit in range(1, 11):
        backtracking(n, 0, target_digit)
