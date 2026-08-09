from collections import deque

def solution(maps):
    maps = [list(row) for row in maps]  # 할당을 위해 str를 리스트로 쪼개준다
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    answer = []
    
    h = len(maps)
    w = len(maps[0])
    
    # dfs, 방문한 곳은 X로 바꾸기
    for i in range(h):
        for j in range(w):
            # 만약 X이면 넘어가기
            if maps[i][j] == 'X':
                continue
                
            # X가 아니면 dfs 들어가기
            Q = deque([(i, j)])
            tmp_sum = int(maps[i][j])  # 연결된 무인도의 식량의 합
            maps[i][j] = 'X'
            
            while Q:
                curX, curY = Q.popleft()
                for d in range(4):
                    nx = curX + dx[d]
                    ny = curY + dy[d]
                    if nx < 0 or nx >= h or ny < 0 or ny >= w:  # 범위 밖이면 pass
                        continue
                    if maps[nx][ny] == 'X':  # 주변이 X이면 pass
                        continue
                    tmp_sum += int(maps[nx][ny])
                    Q.append((nx, ny))
                    maps[nx][ny] = 'X'
                    
            answer.append(tmp_sum)
            
    # answer에 값 들어왔으면 오름차순 return 아니면 -1 반환
    return sorted(answer) if answer else [-1]