def solution(intStrs, k, s, l):
    answer = []
    
    for intStr in intStrs:
        num = int(intStr[s:s+l])
        if num > k: answer.append(num)
    
    return answer