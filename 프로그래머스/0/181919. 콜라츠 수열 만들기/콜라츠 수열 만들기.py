def solution(n):
    answer = [n]
    
    while n != 1:
        # 짝수일 때
        if n % 2 == 0:
            n = n // 2
            answer.append(n)
        # 홀수일 때
        else:
            n = 3 * n + 1
            answer.append(n)
            
    return answer