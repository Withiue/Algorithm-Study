dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]  # 우, 하, 좌, 상 순서

def solution(n):
    answer = [[0]*n for _ in range(n)]
    
    d = 0
    x, y = 0, 0
    
    # 못 움직이면 방향 전환
    for now in range(1, n*n+1):
        answer[x][y] = now
        
        nx = x + dx[d]
        ny = y + dy[d]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        
        x, y = nx, ny
        
    
    return answer