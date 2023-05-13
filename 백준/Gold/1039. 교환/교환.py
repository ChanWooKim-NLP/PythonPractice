from collections import deque, defaultdict

# n은 문자열로, k는 정수형으로 입력 받음
n, k = input().split()
k = int(k)

def bfs():
    max_number = 0
    visited = defaultdict(int)
    visited[(n, 0)] = 1
    queue = deque([(n, 0)])
    
    while queue:
        number, change_cnt = queue.popleft()
        
        if change_cnt == k:
            max_number = max(max_number, int(number))
            continue
        
        number_list = list(number)
        for i in range(len(number_list)-1):
            for j in range(i+1, len(number_list)):
                # 교환 후 맨 앞자리가 0인 경우는 제외
                if i == 0 and number_list[j] == '0':
                    continue
                
                # 위치 교환
                number_list[i], number_list[j] = number_list[j], number_list[i]
                
                # 리스트를 하나의 숫자로 합쳐줌
                number = ''.join(number_list)
                
                # 교환 횟수까지 포함하여 방문 배열에 저장
                if not visited[(number, change_cnt+1)]:
                    visited[(number, change_cnt+1)] = 1
                    queue.append((number, change_cnt+1))
                
                # 원상복구
                number_list[i], number_list[j] = number_list[j], number_list[i]
                    
    return max_number

ans = bfs()

if ans == 0:
    print(-1)
    
else:
    print(ans)