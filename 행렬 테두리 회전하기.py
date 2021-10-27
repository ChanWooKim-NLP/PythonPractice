def rotation(matrix, query):
    # 파이썬 형식으로 좌표 변환
    x1, y1 = query[0] - 1, query[1] - 1
    x2, y2 = query[2] - 1, query[3] - 1

    # 회전 전 좌표 변수 저장 (변수에 저장)
    row1 = matrix[x1][y1:y2]
    row2 = matrix[x2][y1 + 1:y2 + 1]
    col1 = [matrix[x][y1] for x in range(x1 + 1, x2 + 1)]
    col2 = [matrix[x][y2] for x in range(x1, x2)]

    # 가로축 시계방향 회전
    matrix[x1][y1 + 1:y2 + 1] = row1
    matrix[x2][y1:y2] = row2

    # 세로축 시계방향 회전
    # 초기 좌표정보의 보존을 위해 임시변수 x 선언
    # 위로 이동하는 세로축
    x = x1
    for c in range(len(col1)):
        matrix[x][y1] = col1[c]
        x += 1

    # 아래로 이동하는 세로축
    x = x1 + 1
    for c in range(len(col2)):
        matrix[x][y2] = col2[c]
        x += 1

    # 회전 전후 최소값은 같으므로, 다음 회전을 위해 회전된 행렬과 최소값 모두 반환
    minimum = min(row1 + row2 + col1 + col2)

    return matrix, minimum


def solution(rows, columns, queries):
    if rows == 2 and columns == 2:
        return 1

    answer = []

    # 행렬 생성
    matrix = [[i + (rows * c) + 1 for i in range(rows)] for c in range(columns)]

    for q in queries:
        matrix, minimum = rotation(matrix, q)
        answer.append(minimum)

    return answer
