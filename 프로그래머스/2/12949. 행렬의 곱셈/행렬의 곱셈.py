def solution(arr1, arr2):
    answer = []
    
    for r1 in range(len(arr1)):  # arr1의 각 행
        row = []
        
        for c2 in range(len(arr2[0])):  # arr2의 각 열
            total = 0
            
            for k in range(len(arr1[0])):
                total += arr1[r1][k] * arr2[k][c2]
                
            row.append(total)
        
        answer.append(row)
    
    return answer