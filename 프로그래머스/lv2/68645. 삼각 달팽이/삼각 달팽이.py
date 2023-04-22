def solution(n):
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n
    
    answer = []
    
    arr = [
        [0] * n
        for _ in range(n)
    ]
    
    dxs, dys = [1, 0, -1], [0, 1, -1]
    
    # 아래 -> 오른쪽 -> 대각선 위 순으로 배열 채우기 진행
    cur_dir = 0
    x, y = 0, 0
    
    i = 1
    total_cnt = n*(n+1) // 2
    
    while i != total_cnt + 1:
        arr[x][y] = i
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        
        # 다음 위치에 범위를 벗어나거나 값이 이미 적힌 경우 방향 전환 
        if not in_range(nx, ny) or arr[nx][ny]:
            cur_dir = (cur_dir + 1) % 3
            nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        
        x, y = nx, ny
        i += 1
        
    for i in range(n):
        for j in range(i+1):
            answer.append(arr[i][j])
            
    return answer