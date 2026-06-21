def solution(n):
    answer = 0
    
    if n % 2 == 0:  # 짝수
        for num in range(2, n + 1, 2):
            answer += num * num
    else:  # 홀수
        answer = (n + 1) // 2 * (n // 2 + 1)
            
    return answer