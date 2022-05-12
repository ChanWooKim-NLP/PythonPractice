def solution():
    N, M = map(int, input().split())
    chess = []
    result = []
    for _ in range(N):
        chess.append(input())
    
    # 전체 체스판에서 8x8 순회
    for i in range(N-7):
        for j in range(M-7):
            # 시작하는 색에 따라 바뀌는 체스판 개수
            index_W = 0
            index_B = 0
            for k in range(i, i+8):
                for l in range(j, j+8):
                    # 행과 열의 합이 짝수라면 시작점과 같은 색 (0,0이 검은색이면 0,2 / 1,1도 검은색)
                    # 홀수라면 시작점과 다른 색
                    if (k+l) % 2 == 0:
                        if chess[k][l] != 'W':
                            index_W += 1
                        if chess[k][l] != 'B':
                            index_B += 1
                    
                    # 색을 칠할 수 있는 모든 경우의 수 탐색
                    else:
                        if chess[k][l] != 'B':
                            index_W += 1
                        if chess[k][l] != 'W':
                            index_B += 1
        
        # 각 8x8마다 칠할 수 있는 체스판 개수를 담음
        result.append(index_W)
        result.append(index_B)
        
    return min(result)

print(solution())
