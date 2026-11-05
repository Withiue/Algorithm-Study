def solution(n, info):
    answer = [-1]
    max_diff = 0
    ryan = [0] * 11

    def dfs(idx, remain):
        nonlocal answer, max_diff

        # 0점에 도착하면 남은 화살을 모두 사용
        if idx == 10:
            ryan[10] = remain

            ryan_score = 0
            apeach_score = 0

            # 10점부터 1점까지 점수 계산
            for i in range(10):
                score = 10 - i

                if ryan[i] > info[i]:
                    ryan_score += score
                elif info[i] > 0:
                    apeach_score += score

            diff = ryan_score - apeach_score

            # 라이언이 이기는 경우만 정답 후보로 선택
            if diff > 0:
                if diff > max_diff:
                    max_diff = diff
                    answer = ryan[:]

                elif diff == max_diff:
                    # 0점부터 비교하여
                    # 낮은 점수에 더 많이 쏜 경우 선택
                    for i in range(10, -1, -1):
                        if ryan[i] > answer[i]:
                            answer = ryan[:]
                            break
                        elif ryan[i] < answer[i]:
                            break

            # 다른 경우를 탐색하기 위해 초기화
            ryan[10] = 0
            return

        # 현재 점수를 얻으려면 필요한 화살 수
        need = info[idx] + 1

        # 1. 현재 점수를 가져가는 경우
        if remain >= need:
            ryan[idx] = need
            dfs(idx + 1, remain - need)

            # 탐색이 끝나면 쏜 화살 수를 원래대로 복구
            ryan[idx] = 0

        # 2. 현재 점수를 포기하는 경우
        dfs(idx + 1, remain)

    # 10점부터 시작, 사용할 수 있는 화살은 n개
    dfs(0, n)

    return answer