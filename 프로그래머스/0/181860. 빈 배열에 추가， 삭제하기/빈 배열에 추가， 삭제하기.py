def solution(arr, flag):
    X = []
    N = len(arr)
    for i in range(N):
        if flag[i]:
            X.extend([arr[i]] * arr[i] * 2)
        else:
            X = X[:len(X)-arr[i]]
    return X