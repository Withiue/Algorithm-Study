# stack을 사용해야 하는 괄호 문제
# 괄호가 열렸으면 제대로 닫혀야 한다.


def solution(s):
    stk = 0
    for c in s:
        if c == '(':  # 여는 괄호면 stk += 1
            stk += 1
        else:
            if stk > 0:  # 닫는 괄호인데 이전에 열린 괄호 있으면 stk -=1
                stk -= 1
            else:  # 열린 괄호 없으면 False return
                return False
            
    return False if stk else True  # stk에 남은 열린 괄호 있으면 False, 없으면 True 리턴
    