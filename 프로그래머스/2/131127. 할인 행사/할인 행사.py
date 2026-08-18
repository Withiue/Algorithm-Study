from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    # want:number를 Counter로 만들기
    want_counter = Counter(dict(zip(want, number)))
    
    # n 구하기 -> 이만큼 discount를 슬라이딩 윈도우 적용할것임
    n = sum(number)
    
    # discount 순회하며 슬라이딩 윈도우
    for i in range(len(discount) - n + 1):
        
        window = Counter(discount[i:i + n])
        
        # Counter 두 개 끼리 == 비교해서 종류와 개수가 같은지 확인
        if window == want_counter:
            answer += 1
    
    return answer