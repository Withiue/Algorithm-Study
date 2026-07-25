def solution(msg):
    answer = []
    msg = list(msg[::-1])  # stk으로 쓸거임
    
    # 사전 만들기  {'A': 1, ...}
    lzw_dict = {}
    for i in range(1, 27):
        lzw_dict[chr(65+i-1)] = i

    i = 27
    while msg:
        w = msg.pop()  # 현재 입력
        
        while msg:
            c = msg.pop()
            tmp = w + c
            
            if tmp in lzw_dict:
                w = tmp
            else:
                # 현재까지 찾은 가장 긴 문자열 추가
                answer.append(lzw_dict[w])  
                
                # 새로운 문자열 w+c 등록
                lzw_dict[tmp] = i
                i += 1
                
                # c는 아직 처리하지 않았으므로 다시 스택에 넣음
                msg.append(c)                
                break
        else:
            # 남은 입력을 전부 합친 문자열이 사전에 있는 경우
            answer.append(lzw_dict[w]) 
       
    return answer