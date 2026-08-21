def solution(n, info):
    answer = [-1]
    max_diff = 0

    r_board = [0] * 11

    def calc_score():
        apeach = 0
        ryan = 0

        for i in range(11):
            score = 10 - i

            if info[i] == 0 and r_board[i] == 0:
                continue

            if r_board[i] > info[i]:
                ryan += score
            else:
                apeach += score

        return ryan - apeach

    def is_better(new_board, old_board):
        # 점수 차가 같으면 낮은 점수를 더 많이 맞힌 경우 선택
        for i in range(10, -1, -1):
            if new_board[i] > old_board[i]:
                return True
            elif new_board[i] < old_board[i]:
                return False

        return False

    def recur(idx, arrow):
        nonlocal answer, max_diff

        # 모든 점수대를 확인했을 때
        if idx == 11:
            # 남은 화살은 0점에 몰아주기
            remain = n - arrow
            r_board[10] += remain

            diff = calc_score()

            # 라이언이 이긴 경우만 확인
            if diff > 0:
                if diff > max_diff:
                    max_diff = diff
                    answer = r_board[:]

                elif diff == max_diff:
                    if answer == [-1] or is_better(r_board, answer):
                        answer = r_board[:]

            # 백트래킹
            r_board[10] -= remain
            return

        need = info[idx] + 1

        # 1. 현재 점수를 가져가는 경우
        if arrow + need <= n:
            r_board[idx] = need

            recur(
                idx + 1,
                arrow + need
            )

            # 백트래킹
            r_board[idx] = 0

        # 2. 현재 점수를 포기하는 경우
        recur(
            idx + 1,
            arrow
        )

    recur(0, 0)

    return answer