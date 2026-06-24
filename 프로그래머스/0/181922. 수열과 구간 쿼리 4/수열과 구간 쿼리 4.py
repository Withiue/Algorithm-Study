def solution(arr, queries):
    
    for s, e, k in queries:
        for i in range(s, e + 1):
            # i가 k의 배수이면 arr[i]에 1을 더하기
            if i % k == 0:
                arr[i] += 1
    
    return arr