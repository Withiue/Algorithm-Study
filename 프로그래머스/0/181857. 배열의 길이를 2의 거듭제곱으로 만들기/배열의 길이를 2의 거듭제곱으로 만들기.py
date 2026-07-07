def solution(arr):
    n = len(arr)
    
    i = 1
    while i <= 1025:
        if n <= i:
            arr.extend([0] * (i - n))
            break
        
        i *= 2
    return arr