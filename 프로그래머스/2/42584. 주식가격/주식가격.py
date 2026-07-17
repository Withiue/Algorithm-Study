from collections import deque

def solution(prices):
    answer = []
    Q = deque(prices)
    
    while Q:
        cur_price = Q.popleft()
        tmp = 0
        for q in Q:
            tmp += 1
            if cur_price > q:
                break
        answer.append(tmp)
                      
    return answer