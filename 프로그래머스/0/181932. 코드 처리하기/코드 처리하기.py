def solution(code):
    ret = ''
    
    mode = 0
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == "1":
                mode = 1
            elif idx % 2 == 0:
                ret += code[idx]
        elif mode == 1:
            if code[idx] == "1":
                mode = 0
            elif idx % 2 == 1:
                ret += code[idx]
    
    # 빈 문자열 처리
    return "EMPTY" if ret == '' else ret