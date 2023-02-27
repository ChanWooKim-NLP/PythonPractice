n, m = map(int, input().split())

sub_ans = []

# index 별 방문 여부
visited = [0] * n

# 백트래킹
# 수열 길이가 m이 될 때 까지 수 선택
# 선택 완료된 수열이 이미 print 되었으면 중복

# 배열은 정렬된 상태에서 백트래킹 시작

# idx : 탐색을 시작할 인덱스, 처음엔 0부터 n까지 탐색
# 선택한 후, 해당 인덱스부터 n까지 탐색하여 추가하면 조건을 만족함
# 예시) 4 2 / 9 7 9 1 케이스에서 1 7 9 9로 정렬되고, 7이 선택되면 인덱스 1부터 선택 진행
# A[i] <= A[i+1] ... <= A[k]
def backtracking(length, idx):
    if idx == n+1:
        return
    
    prev = 0
    if length == m:
        int_seq = ' '.join(map(str, sub_ans))
        print(int_seq)
        return
    
    for i in range(idx, n):
        if not visited[i] and arr[i] != prev:
            prev = arr[i]
            sub_ans.append(arr[i])
            visited[i] = True
        
            backtracking(length+1, i+1)
            
            visited[i] = False
            sub_ans.pop()
    
    
arr = sorted(list(map(int, input().split())))
backtracking(0, 0)