def solution(board):
    m = len(board)
    n = len(board[0])

    max_size = 0  # 가장 큰 정사각형의 한 변 길이

    for i in range(m):
        for j in range(n):

            # 0이면 정사각형을 만들 수 없으므로 넘어감
            if board[i][j] == 0:
                continue

            # 첫 번째 행, 첫 번째 열은 주변 3칸을 볼 수 없으므로 제외
            if i > 0 and j > 0:

                # 위, 왼쪽, 왼쪽 위 중
                # 가장 작은 값 + 1
                #
                # => 현재 칸까지 포함해서 만들 수 있는
                #    가장 큰 정사각형의 한 변 길이
                board[i][j] = min(
                    board[i - 1][j],      # 위
                    board[i][j - 1],      # 왼쪽
                    board[i - 1][j - 1]   # 왼쪽 위
                ) + 1

            # 가장 큰 한 변 길이 저장
            max_size = max(max_size, board[i][j])

    # 한 변 × 한 변 = 넓이
    return max_size * max_size