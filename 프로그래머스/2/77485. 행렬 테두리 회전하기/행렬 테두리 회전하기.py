def solution(rows, columns, queries):
    answer = []

    # 1부터 rows * columns까지 행렬 만들기
    board = []
    num = 1

    for i in range(rows):
        tmp = []

        for j in range(columns):
            tmp.append(num)
            num += 1

        board.append(tmp)

    # 각 회전 명령 처리
    for x1, y1, x2, y2 in queries:

        # 인덱스를 0부터 시작하도록 변경
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        # 왼쪽 위 값을 임시 저장
        temp = board[x1][y1]
        min_value = temp

        # 왼쪽 변: 아래 값을 위로 이동
        for i in range(x1, x2):
            board[i][y1] = board[i + 1][y1]
            min_value = min(min_value, board[i][y1])

        # 아래쪽 변: 오른쪽 값을 왼쪽으로 이동
        for j in range(y1, y2):
            board[x2][j] = board[x2][j + 1]
            min_value = min(min_value, board[x2][j])

        # 오른쪽 변: 위 값을 아래로 이동
        for i in range(x2, x1, -1):
            board[i][y2] = board[i - 1][y2]
            min_value = min(min_value, board[i][y2])

        # 위쪽 변: 왼쪽 값을 오른쪽으로 이동
        for j in range(y2, y1 + 1, -1):
            board[x1][j] = board[x1][j - 1]
            min_value = min(min_value, board[x1][j])

        # 처음 저장해둔 왼쪽 위 값을 옆 칸에 넣기
        board[x1][y1 + 1] = temp

        answer.append(min_value)

    return answer