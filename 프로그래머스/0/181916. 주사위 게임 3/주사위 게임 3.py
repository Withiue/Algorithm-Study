def solution(a, b, c, d):
    answer = 0
    
    # 무슨 숫자 나왔는지 횟수 기록
    dice_num_board = [0] * 7
    
    for score in [a, b, c, d]:
        dice_num_board[score] += 1
    print(dice_num_board)
    
    
    # 1. 모두 같은 숫자
    if 4 in dice_num_board:
        answer += 1111 * a
    # 2. 세 개가 같음
    elif 3 in dice_num_board:
        p = dice_num_board.index(3)
        q = dice_num_board.index(1)
        answer += (10 * p + q) ** 2
    # 3. 두 개씩 같음
    elif 2 in dice_num_board and 1 not in dice_num_board:
        p, q = [i for i in range(1, 7) if dice_num_board[i] == 2]
        answer += (p + q) * abs(p - q)
    # 4. 두 개 같음, 하나 하나 다름
    elif 2 in dice_num_board and 1 in dice_num_board:
        q, r = [i for i in range(1, 7) if dice_num_board[i] == 1]
        answer += q * r
    # 5. 모두 다름
    else:
        answer += min(a, b, c, d)
        
    return answer