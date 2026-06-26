def solution(s):
    answer = True
    
    s = s.lower()  # 모두 소문자로 변환
    
    p_num = s.count('p')
    y_num = s.count('y')

    if p_num > 0 and y_num > 0 and p_num == y_num:  # 개수 비교 같을 때
        return True
    elif p_num == 0 and y_num == 0:  # 둘 다 0일때
        return True
    else:  # 그 외
        return False