def solution(arr):
    stk = []
    i = 0  # 초기값 설정
    while i < len(arr):
        if stk:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk = stk[:-1]
        else:
            stk.append(arr[i])
            i += 1
    return stk