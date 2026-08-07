# 틱택토에서 나올 수 있는 경우면 1, 아니며 0 리턴하기

# 나올 수 있는 경우
# 1. 빙고 한 명만 나온 경우
# 1-1. 선공이 빙고면 후공 = 선공 - 1개 있어야 함
# 1-2. 후공이 빙고면 선공 = 후공 개수 같아야 함

# 빙고 안 나온 경우
# 1. 아예 빈 칸
# 2. 빙고 없고, 선공이 후공보다 개수 같거나 많음

# 이외의 경우는 나올 수 없음
# 빙고 두 개면 탈락

def solution(board):        
    # player(O, X)가 빙고인지 여부 구하는 함수
    def is_bingo(player):
        # 가로 연속 세 개면 빙고
        for b in board:
            if b == player * 3:
                return True
            
        # 세로 연속 세 개면 빙고
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True
            
        # 대각선 연속 세 개면 빙고
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        
        return False
        
    # O, X 개수 세기
    cnt_O, cnt_X = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X': cnt_X += 1
            if board[i][j] == 'O': cnt_O += 1
    
    # 돌 개수 자체가 불가능한 경우
    if not (cnt_O == cnt_X or cnt_O == cnt_X + 1):
        return 0
    
    # 빙고 나온 경우
    o_bingo = is_bingo('O')
    x_bingo = is_bingo('X')
    
    # 1. 둘 다 빙고일 수 없다
    if o_bingo and x_bingo:
        return 0
    
    # 2. 한 명의 빙고가 나온 경우
    # 2-1. 선공이 빙고면 선공이 마지막으로 둬야함
    if o_bingo:
        return 1 if cnt_O == cnt_X + 1 else 0
    # 2-2. 후공이 빙고면 후공이 마지막으로 둬야함
    if x_bingo:
        return 1 if cnt_O == cnt_X else 0
    
    # 빙고 없고 돌 개수 정상
    return 1