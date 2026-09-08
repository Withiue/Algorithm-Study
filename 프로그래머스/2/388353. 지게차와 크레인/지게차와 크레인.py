from collections import deque

def solution(storage, requests):
    answer = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    n = len(storage) + 2
    m = len(storage[0]) + 2

    # 테두리를 '.'로 감싸기
    s_lst = [['.' for _ in range(m)] for _ in range(n)]

    for i in range(n - 2):
        for j in range(m - 2):
            s_lst[i + 1][j + 1] = storage[i][j]

    # 지게차
    def fork_lift(r):
        visited = [[False for _ in range(m)] for _ in range(n)]

        Q = deque([(0, 0)])
        visited[0][0] = True

        while Q:
            curX, curY = Q.popleft()

            for d in range(4):
                nx = curX + dx[d]
                ny = curY + dy[d]

                # 범위 밖
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                # 이미 방문
                if visited[nx][ny]:
                    continue

                # 빈 공간이면 이동 가능
                if s_lst[nx][ny] == '.':
                    visited[nx][ny] = True
                    Q.append((nx, ny))

                # 원하는 컨테이너면 제거
                elif s_lst[nx][ny] == r:
                    s_lst[nx][ny] = '.'
                    visited[nx][ny] = True

    # 크레인
    def crane(r):
        for i in range(n):
            for j in range(m):
                if s_lst[i][j] == r:
                    s_lst[i][j] = '.'

    # 요청 처리
    for r in requests:
        if len(r) == 1:
            fork_lift(r)

        elif len(r) == 2:
            crane(r[0])

    # 남은 컨테이너 개수
    for i in range(n):
        for j in range(m):
            if s_lst[i][j] != '.':
                answer += 1

    return answer