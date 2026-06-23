def solution(numLog):
    result = ''
    
    control = { 1: 'w', -1: 's', 10: 'd', -10: 'a' }
    
    for i in range(1, len(numLog)):
        c = numLog[i] - numLog[i - 1]  # 그 전과의 차이값
        result += control[c]
    
    return result