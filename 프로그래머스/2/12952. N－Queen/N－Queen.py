def solution(n):
    answer = 0

    # 이미 퀸이 존재하는 열
    cols = set()

    # 이미 퀸이 존재하는 대각선
    diag1 = set()   # row - col
    diag2 = set()   # row + col

    def dfs(row):
        nonlocal answer

        # 1. 모든 행에 퀸을 배치했다면 answer += 1
        if row == n:
            answer += 1
            return

        # 현재 row의 모든 열을 하나씩 확인
        for col in range(n):

            # 2. 현재 위치 (row, col)에
            # 퀸을 놓을 수 없는 경우를 검사
            if col in cols or row - col in diag1 or row + col in diag2:
                continue

            # 3. 현재 위치에 퀸을 놓았다고 기록
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            # 4. 다음 행으로 이동
            dfs(row + 1)

            # 5. 현재 퀸을 제거하고 원상복구
            # → 다음 col도 확인해야 하기 때문
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    dfs(0)

    return answer