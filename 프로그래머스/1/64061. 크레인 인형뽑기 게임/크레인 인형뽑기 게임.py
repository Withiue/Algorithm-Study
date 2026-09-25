def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        col = move - 1  # moves는 1부터 시작하므로 인덱스로 변환

        # 해당 열에서 가장 위에 있는 인형 찾기
        for row in range(len(board)):
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0

                # 바구니 마지막 인형과 같으면 두 개 제거
                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)

                break  # 한 번의 집게 동작 종료

    return answer