from collections import deque

def solution(maps):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    rows = len(maps)
    cols = len(maps[0])

    # 1. S, E, L 위치 구하기
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'E':
                E = (i, j)
            elif maps[i][j] == 'L':
                L = (i, j)

    # 2. BFS로 시작 지점 -> 레버 최단 이동 시간 구하기
    Q = deque([(S[0], S[1], 0)])  # 행, 열, 이동 시간
    visited = [[False] * cols for _ in range(rows)]
    visited[S[0]][S[1]] = True

    time_to_lever = -1

    while Q:
        x, y, time = Q.popleft()

        if (x, y) == L:
            time_to_lever = time
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 지도 범위 안에 있는지 확인
            if 0 <= nx < rows and 0 <= ny < cols:
                # 벽이 아니고 아직 방문하지 않았다면 이동
                if maps[nx][ny] != 'X' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    Q.append((nx, ny, time + 1))

    # 레버에 도달할 수 없다면 탈출 불가능
    if time_to_lever == -1:
        return -1

    # visited 초기화
    visited = [[False] * cols for _ in range(rows)]

    # 3. BFS로 레버 -> 출구 최단 이동 시간 구하기
    Q = deque([(L[0], L[1], 0)])
    visited[L[0]][L[1]] = True

    time_to_exit = -1

    while Q:
        x, y, time = Q.popleft()

        if (x, y) == E:
            time_to_exit = time
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < rows and 0 <= ny < cols:
                if maps[nx][ny] != 'X' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    Q.append((nx, ny, time + 1))

    # 출구에 도달할 수 없다면 탈출 불가능
    if time_to_exit == -1:
        return -1

    # 4. 두 이동 시간을 합해서 반환
    answer = time_to_lever + time_to_exit
    return answer