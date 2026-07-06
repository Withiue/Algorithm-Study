# 최대한 많은 부서에 예산 안에서 지원

# 1. 적은 예산 순으로 예산을 sorting
# 2. 앞에서부터 지원해줌, budget 부족 시 카운트 안 함

def solution(d, budget):
    answer = 0  # 지원한 부서 수
    
    d.sort()  # 적은 예산 먼저 지원해주기 위해 예산 sorting

    for price in d:
        # 만약 budget 부족 시 break
        if price > budget:
            break
        
        # 지원 가능이면 지원금만큼 budget에서 차감, 지원한 부서 수(answer) +1
        budget -= price
        answer += 1
        
    return answer