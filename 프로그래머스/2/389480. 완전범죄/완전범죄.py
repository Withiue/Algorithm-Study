def solution(info, n, m):
    # dp[b 흔적] = 해당 b 흔적일 때 최소 a 흔적
    # a 흔적은 n 이상이면 잡히므로 n을 불가능 상태로 사용
    INF = n

    dp = [INF] * m
    dp[0] = 0

    # 물건 하나씩 확인
    for a, b in info:
        new_dp = [INF] * m

        for cur_b in range(m):

            # 만들 수 없는 상태
            if dp[cur_b] == INF:
                continue

            cur_a = dp[cur_b]


            # 1. A가 훔치는 경우
            next_a = cur_a + a

            if next_a < n:
                new_dp[cur_b] = min(
                    new_dp[cur_b],
                    next_a
                )


            # 2. B가 훔치는 경우
            next_b = cur_b + b

            if next_b < m:
                new_dp[next_b] = min(
                    new_dp[next_b],
                    cur_a
                )

        dp = new_dp


    # 모든 물건을 훔친 뒤 최소 A 흔적
    answer = min(dp)

    if answer == INF:
        return -1

    return answer