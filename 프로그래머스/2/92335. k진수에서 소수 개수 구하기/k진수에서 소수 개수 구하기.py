# n을 k진수로 바꾸기
# 0으로 split()하기
# split()한 것들이 소수인지 각각 판별하기

import math

def solution(n, k):
    answer = 0
    
    # n을 k진수로 변환
    tmp = []
    while n >= k:
        tmp.append(str(n % k))
        n //= k
    tmp.append(str(n))
    k_num = ''.join(reversed(tmp))
    
    # k_num을 0으로 split()하기
    candidate = k_num.split('0')
    candidate = [int(c) for c in candidate if c]  # 공백 없애고 int로 바꾸기
    
    # split()한 것들이 소수인지 각각 판별하기
    # 소수: 나와 1밖에 나눠지는 수가 없는 것
    for c in candidate:
        if c == 1: continue  # 1 거르기
        
        # 소수인지 확인
        for i in range(2, int(math.sqrt(c)) + 1):
            
            # 자기 자신이면 pass
            if c == i: continue
            
            # 자기 자신이 아닌 수로 나눠 떨어지면 소수가 아님
            if c % i == 0: break
        
        # 소수 맞으면 answer += 1 하기
        else:
            answer += 1
            
    
    return answer