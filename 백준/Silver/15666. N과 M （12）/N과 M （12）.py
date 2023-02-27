n, m = map(int, input().split())

sub_ans = []

# index 별 방문 여부

# 백트래킹
# 수열 길이가 m이 될 때 까지 수 선택
# 선택 완료된 수열이 이미 print 되었으면 중복

# 중복을 허락하므로 방문 배열 사용하지 않음
# 비내림차순이므로 추가한 수보다 크거나 같은 수를 수열에 추가해야 함
# 탐색한 index에서 백트래킹 진행
def backtracking(length, idx):
    prev = 0
    if length == m:
        int_seq = ' '.join(map(str, sub_ans))
        print(int_seq)
        return
    
    for i in range(idx, n):
        if prev != arr[i]:
            prev = arr[i]
            
            sub_ans.append(arr[i])
            backtracking(length+1, i)
            sub_ans.pop()
    
    
arr = sorted(list(map(int, input().split())))
backtracking(0, 0)

