n, m = map(int, input().split())

sub_ans = []

# index 별 방문 여부
visited = [0] * n

# 백트래킹
# 수열 길이가 m이 될 때 까지 수 선택
# 선택 완료된 수열이 이미 print 되었으면 중복

# for문으로 인덱스 순회하면서 방문 안한 인덱스 선택
# 중복 방지 위해 prev 변수로 arr[i] 기록하여 한 번 선택한 인덱스의 중복 선택 방지
def backtracking(length):
    prev = 0
    if length == m:
        int_seq = ' '.join(map(str, sub_ans))
        print(int_seq)
        return
    
    for i in range(n):
        if not visited[i] and arr[i] != prev:
            prev = arr[i]
            sub_ans.append(arr[i])
            visited[i] = True
            
            backtracking(length+1)
            
            visited[i] = False
            sub_ans.pop()
    
    
arr = sorted(list(map(int, input().split())))
backtracking(0)