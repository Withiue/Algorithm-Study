def solution(order):
    answer = 0
    
    for o in order:
        # 아메리카노, 아무거나 4500원
        if 'americano' in o or 'anything' in o:
            answer += 4500
        
        # 카페라테 5000원
        elif 'latte' in o:
            answer += 5000
            
    return answer