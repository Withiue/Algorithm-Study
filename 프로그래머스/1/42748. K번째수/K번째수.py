def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        
        # 1. 자르기
        tmp = array[i-1:j]
        
        # 2. 정렬하기
        tmp.sort()
        
        # 3. k번째 숫자 구하기, answer에 담기
        answer.append(tmp[k-1])

    return answer