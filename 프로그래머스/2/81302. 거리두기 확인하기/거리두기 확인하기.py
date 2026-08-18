# 맨해튼 거리(Manhattan distance)는 격자 모양으로 반듯하게 뻗은 도시(미국 뉴욕 맨해튼)에서 유래한 개념으로, 좌표 평면 위에서 두 점 사이의 거리를 측정할 때 대각선이 아닌 가로와 세로(수평 및 수직) 방향 이동 거리의 합으로 계산하는 방식입니다.
# 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, 
# T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다.

# P 응시자, O 빈 테이블, X 파티션
# 맨해튼 거리 2 초과 - 모두 허용 (여기부터는 볼 필요 X)
# 맨해튼 거리 2 - 사이에 빈 테이블(O) 있으면 비허용, 모두 파티션(X)이면 허용
# 맨해튼 거리 0, 1 - 무조건 비허용

from collections import deque

def solution(places):
    answer = []  # 거리두기 지켜지면 1, 아니면 0 담기
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    for place in places:
        is_safe = True
        
        # 모든 칸 확인
        for i in range(5):
            for j in range(5):
                
                # 사람이 아니면 넘어감
                if place[i][j] != 'P':
                    continue
                
                # 현재 사람을 기준으로 BFS 초기화
                Q = deque([(i, j, 0)])  # (x, y, dist)
                visited = [[False] * 5 for _ in range(5)]
                visited[i][j] = True
                
                while Q:
                    curX, curY, dist = Q.popleft()
                    
                    # 거리가 2가 되면 더 이상 이동할 필요 없음 (2 초과는 모두 허용)
                    if dist == 2:
                        continue
                    
                    for d in range(4):
                        nx = curX + dx[d]
                        ny = curY + dy[d]
                        
                        # 범위 밖이면 continue
                        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                            continue
                        
                        # 이미 방문했으면 continue
                        if visited[nx][ny]:
                            continue
                        
                        # 파티션이면 continue
                        if place[nx][ny] == 'X':
                            continue
                        
                        # 다른 사람 만나면 거리두기 실패
                        if place[nx][ny] == 'P':
                            is_safe = False
                            break
                            
                        # 빈 테이블이면 계속 탐색
                        visited[nx][ny] = True
                        Q.append((nx, ny, dist + 1))
                    
                    if not is_safe:
                        break
                
                if not is_safe:
                    break
        
        if is_safe:
            answer.append(1)
        else:
            answer.append(0)
        
    return answer