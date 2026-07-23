def solution(n, t, m, p):
    answer = ''
    digits = '0123456789ABCDEF'
    
    num = 0  # 십진수, 현재 숫자
    while num < t * m:  # (미리 구할 숫자의 갯수 t) * (게임에 참가하는 인원 m) 만큼 구해놓는다.
        
        # 십진수 num을 n진수로 바꾸기
        n_num = ''
        tmp_num = num
        while tmp_num >= n:
            n_num += digits[tmp_num % n]
            tmp_num //= n
        n_num += digits[tmp_num]
        
        answer += n_num[::-1]
        
        num += 1
    
    # 튜브가 말해야 하는 숫자 구하기    
    return answer[p-1::m][:t]
    