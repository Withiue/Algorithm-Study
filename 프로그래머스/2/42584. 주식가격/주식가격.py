from collections import deque

def solution(prices):
    answer = []
    Q = deque(prices)
    
    while Q:
        cur = Q.popleft()
        tmp = 0
        for q in Q:
            tmp += 1  # 떨어지기 직전까지를 1초로 센다
            if cur > q:
                break
        answer.append(tmp)
        
    return answer