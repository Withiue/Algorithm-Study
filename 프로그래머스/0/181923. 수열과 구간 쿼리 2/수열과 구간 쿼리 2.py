def solution(arr, queries):
    result = []
    
    # 쿼리 하나씩 꺼내기
    for s, e, k in queries:
        min_tmp = 1000001  # 지금까지 조건 만족 수 중 최소값
        
        for i in range(s, e + 1):  # i 범위 for문
            if arr[i] > k:  # arr[i]가 k뵤다 크면
                min_tmp = min(min_tmp, arr[i])  # 그 중 최소값 갱신
                
        # min_tmp 값이 바뀌지 않았으면 -1 저장
        if min_tmp == 1000001:
            result.append(-1)
        else:
            result.append(min_tmp)
    
    return result