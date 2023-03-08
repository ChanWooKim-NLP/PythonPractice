def solution(n, wires):
    # dfs로 연결된 송전탑 개수 확인
    def dfs(node):
        nonlocal cnt

        visited[node] = 1
        cnt += 1
        
        for idx in range(n):
            next_node = graphs[node][idx]
            if next_node == 1 and not visited[idx]:
                dfs(idx)        
        
        
        
    graphs = [
        [0] * n
        for _ in range(n)
    ]
    
    for x, y in wires:
        graphs[x-1][y-1] = 1
        graphs[y-1][x-1] = 1
    
    # 개수 차이
    answer = float('inf')
    
    # 전선을 하나씩 끊고 복구하면서 차이 계산
    for x, y in wires:
        # 끊기
        graphs[x-1][y-1] = 0
        graphs[y-1][x-1] = 0
        
        visited = [0] * n
        
        split_cnt = []
        # 모든 노드에 대해 dfs 수행, 2개의 망으로 분리 후 송전탑 개수를 split_cnt에 추가
        for i in range(n):
            if not visited[i]:
                cnt = 0
                dfs(i)
                split_cnt.append(cnt)
        
        answer = min(answer, abs(split_cnt[0] - split_cnt[1]))
        
        # 복구
        graphs[x-1][y-1] = 1
        graphs[y-1][x-1] = 1
        
    return answer