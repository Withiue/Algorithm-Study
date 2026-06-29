def solution(arr, idx):
    result = -1
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            result = i
            break
    return result