# n명의 사람이 돌아가며 끝말잇기
# 이전에 한 적 있으면 짐
# 끝말이 이어지지 않으면 짐
# 질 경우 return
# 이길 경우 다음 사람

def solution(n, words):
    history = []  # 이전에 나왔던 단어들
    
    # 1번 사람부터 시작
    cur_num = 1 
    history.append(words[0])  # 첫 단어 무조건 넣기
    turn = 1  # 몇 바퀴째 돌고 있는지
    cur_num += 1

    for i in range(1, len(words)):
        # 이전에 한 적 있으면 짐
        if words[i] in history:
            return [cur_num, turn]
        
        # 끝 말이 이어지지 않으면 짐
        if words[i][0] != history[-1][-1]:
            return [cur_num, turn]
        
        # 한 턴 다 돌았으면 턴 추가
        history.append(words[i])
        cur_num += 1
        if cur_num > n:
            turn += 1
            cur_num -= n
            
    # 탈락자 없으면 [0, 0] 리턴
    return [0, 0]