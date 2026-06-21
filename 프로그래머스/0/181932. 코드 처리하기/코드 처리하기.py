def solution(code):
    ret = ''
    
    mode = 0
    
    for idx in range(len(code)):
        if code[idx] == "1":
            mode ^= 1
        elif idx % 2 == mode:
            ret += code[idx]
    
    # 빈 문자열 처리
    return ret if ret else "EMPTY"