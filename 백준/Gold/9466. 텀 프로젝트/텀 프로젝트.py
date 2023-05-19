import sys
from collections import defaultdict

sys.setrecursionlimit(1000001)

input = sys.stdin.readline

# 학생 번호, 현재 만들어진 사이클에서 학생의 위치 딕셔너리 파악
def dfs(student_idx, cur=0):
    global answer
    
    arr.append(student_idx)
    visited[student_idx] = 1
    nx_student = want_to_match[student_idx]
    
    # 학생 위치 딕셔너리에 추가된 시간 정보 추가
    idx_loc_dict[student_idx] = cur
    
    if not visited[nx_student]:
        dfs(nx_student, cur+1)
        
    else:
        # 다음 학생이 이미 사이클에 추가되었을 경우
        if nx_student in arr:
            # 해당 학생이 추가된 시간을 찾고
            # 짝을 찾은 리스트에 추가
            cycle_start_idx = idx_loc_dict[nx_student]
            answer.extend(arr[cycle_start_idx:])
        
        return
            
t = int(input())

for _ in range(t):
    n = int(input())
    
    visited = [0] * (n+1)
    
    # 인덱스를 맞추기 위해 제일 첫 인덱스의 값은 0으로 설정
    want_to_match = [0] + list(map(int, input().split()))
    
    answer = []
    for i in range(1, n+1):
        if not visited[i]:
            arr = []
            idx_loc_dict = defaultdict(int)
            dfs(i, 0)
            
    print(n - len(answer))