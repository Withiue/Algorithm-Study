def solution(arr1, arr2):
    answer = []
    n = len(arr2)  # == len(arr1[0])
    
    # arr1 행 순회
    for x1 in range(len(arr1)):
        tmp_lst = []
            
        # arr2 열 순회
        for y2 in range(len(arr2[0])):
            
            tmp_sum = 0
            
            # 행렬곱, k기준 동시 순회
            for k in range(n):
                tmp_sum += arr1[x1][k] * arr2[k][y2]
            
            tmp_lst.append(tmp_sum)
        
        answer.append(tmp_lst)

    return answer