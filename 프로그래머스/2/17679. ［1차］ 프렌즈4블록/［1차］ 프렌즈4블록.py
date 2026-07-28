# 캔디팡 구현
# 처음 팡
# 2*2 슬라이드 순회 검색을 한다.
# 2*2 형태가 있으면 pang이라는 n*m 배열에 1로 그 범위를 색칠한다.
# pang에서 1을 찾아서 그만큼 점수를 더한다.
# pang의 1만큼 board를 X로 바꾼다.(X는 비었다는 의미)

# 밑으로 내리기
# 밑으로 어떻게 내리지?

# 그다음 팡
# 

# 팡이 하나도 없으면 종료, 점수 리턴

def is_pang(i, j, board):
    if board[i][j] == 'X':
        return False
    
    if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
        return True
    
    return False

def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]
    
    while True:
        pang = [[0]*n for _ in range(m)]  # 터뜨려야 할 블록들, 매 턴마다 초기화
        
        # 1. 터뜨릴 블록 찾기
        for i in range(m-1):
            for j in range(n-1):
                if is_pang(i, j, board):
                    pang[i][j], pang[i+1][j], pang[i][j+1], pang[i+1][j+1] = 1, 1, 1, 1

        # 2. 터뜨릴 블록 개수 세고 터뜨리기
        cnt = 0
        for i in range(m):
            for j in range(n):
                if pang[i][j] == 1:
                    board[i][j] = 'X'
                    cnt += 1

        # 이번에 터뜨린 블록이 없다면 게임 종료
        if cnt == 0: break
        
        # 터진 블록 수 누적
        answer += cnt

        # 3. 블록을 아래로 내리기
        # i : 원래 블록을 찾는 위치
        # write : 찾은 블록을 내려놓을 위치
        for j in range(n):
            write = m - 1

            for i in range(m-1, -1, -1):  # 열 하나를 아래에서부터 위로 한 칸씩 올라가기
                if board[i][j] != 'X':
                    board[write][j] = board[i][j]
                    write -= 1

            # 빈 곳을 X로 채우기
            while write >= 0:
                board[write][j] = 'X'
                write -= 1
        
        
    return answer