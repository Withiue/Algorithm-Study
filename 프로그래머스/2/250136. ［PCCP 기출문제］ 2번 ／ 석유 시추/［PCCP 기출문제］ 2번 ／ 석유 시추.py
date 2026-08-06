# 시추 뚫기
# 전체를 dfs하고 몇 번째 열에 걸치는지 확인

# 가장 많은 석유f량 리턴

from collections import deque

def solution(land):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    rows = len(land)
    cols = len(land[0])
    
    # 각 열에 시추관을 꽂았을 때 얻는 석유량
    oil_by_col = [0] * cols
        
    # 모든 칸을 한 번씩 확인
    for start_x in range(rows):
        for start_y in range(cols):
            
            # 벽이거나 이미 방문한 석유라면 넘어감
            if land[start_x][start_y] == 0:
                continue
                
            Q = deque([(start_x, start_y)])
            
            # 방문처리
            land[start_x][start_y] = 0
            
            oil_size = 0
            
            # 현재 석유 덩어리가 걸쳐 있는 열
            touched_cols = set()
            
            while Q:
                cur_x, cur_y = Q.popleft()
                
                oil_size += 1
                touched_cols.add(cur_y)
                
                for d in range(4):
                    nx = cur_x + dx[d]
                    ny = cur_y + dy[d]
                    
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                        continue
                    if land[nx][ny] == 0:
                        continue
                        
                    # 큐에 넣을 때 바로 방문 처리
                    # 그래야 같은 칸이 큐에 여러 번 들어가지 않음
                    land[nx][ny] = 0
                    Q.append((nx, ny))
            
            # 이 석유 덩어리가 걸쳐 있는 모든 열에
            # 덩어리 전체 크기를 한 번씩 더함
            for c in touched_cols:
                oil_by_col[c] += oil_size
    
    return max(oil_by_col)