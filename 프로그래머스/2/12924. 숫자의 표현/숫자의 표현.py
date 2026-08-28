# 투 포인터 - n보다 크면 왼쪽포인터 옮기기(마이너스), n보다 작으면 오른쪽포인터 옮기기(플러스)

def solution(n):
    answer = 0
    
    start = 1
    end = 1
    total = 1
    
    while start <= n:
        
        # n일 때
        if total == n:
            answer += 1
            total -= start
            start += 1  # 시작포인터 한 번 옮기기
        
        # 플러스
        elif total < n:
            end += 1
            total += end
        
        # 마이너스
        elif total > n:
            total -= start
            start += 1
            
    return answer