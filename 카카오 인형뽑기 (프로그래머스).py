def solution(board, moves):
    def To_stack(board):
        new_board = []
        for i in range(len(board)):
            ele = [element[i] for element in board]
            new_board.append(ele)

        return new_board

    new_board = To_stack(board)
    basket = []
    index = 0
    result = 0

    while index != len(moves):
        m = moves[index] - 1

        if not new_board[m]:
            index += 1
            continue
        else:
            doll = new_board[m].pop(0)
            if doll != 0:
                if not basket:
                    basket.append(doll)
                else:
                    index += 1
                    if basket[-1] == doll:
                        basket.pop()
                        result += 2
                    else:
                        basket.append(doll)
    return result

## 두번째 풀이
def solution2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer
