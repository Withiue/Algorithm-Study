def solution(arr):
    h = len(arr)
    w = len(arr[0])
    
    if w < h:
        n = h - w
        for i in range(h):
            arr[i].extend([0 for _ in range(n)])
    elif h < w:
        n = w - h
        for i in range(n):
            arr.append([0 for _ in range(w)])
        
    return arr