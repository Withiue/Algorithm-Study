def solution(arr):
    idx = []
    for i, a in enumerate(arr):
        if a == 2:
            idx.append(i)
    if not idx:
        return [-1]
    elif len(idx) == 1:
        return [2]
    else:
        return arr[idx[0]:idx[-1]+1]