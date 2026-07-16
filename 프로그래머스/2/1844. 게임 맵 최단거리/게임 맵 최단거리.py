# dfs 길찾기 문제
# 모두 visit했는데도 상대팀 못찾으면 -1 return
# 처음에 캐릭터는 게임 맵의 좌측 상단인 (0, 0) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n-1, m-1) 위치에 있습니다.
# 1은 길, 0은 벽

from collections import deque

def solution(maps):
    # 방향 초기화
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    # 초기화
    n, m = len(maps), len(maps[0])
    Q = deque()
    Q.append((0, 0))
    
    # dfs
    while Q:
        cx, cy = Q.popleft()
        
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            
            # maps 범위 밖이면 pass
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            
            # 벽이거나 이미 방문했으면 pass
            if maps[nx][ny] == 0 or maps[nx][ny] > 1: continue
            
            # 이동할 수 있으면 방문처리하기, 다음 방문 가능한 좌표 큐에 넣기
            maps[nx][ny] = maps[cx][cy] + 1
            Q.append((nx, ny))
            
    
    # 만약 (n-1, m-1)이 여전히 1이면 도달 못했으므로 -1 return
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]