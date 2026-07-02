def solution(arr):
    x = 0
    while True:
        new_arr = []
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                new_arr.append(arr[i] // 2)
            elif arr[i] < 50 and arr[i] % 2 == 1:
                new_arr.append(arr[i] * 2 + 1)
            else:
                new_arr.append(arr[i])
        
        if arr == new_arr:
            return x
        else:
            arr = new_arr[:]
            x += 1

        