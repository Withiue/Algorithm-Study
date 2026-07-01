def solution(arr):
    result = []
    
    for a in arr:
        if a >= 50 and a % 2 == 0:
            result.append(a // 2)
        elif a < 50 and a % 2 == 1:
            result.append(a * 2)
        else:
            result.append(a)
            
    return result