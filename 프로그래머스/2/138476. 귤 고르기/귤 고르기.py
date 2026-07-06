# 귤의 종류 최소화 -> 최소 종류값 return
# k개 골라서 판매하고 싶음

# 1. 종류별 귤 개수를 센다.
# 2. 개수가 많은 종류의 귤을 k개 뽑는다.
# 3. 총 종류를 리턴한다.

from collections import Counter

def solution(k, tangerine):
    answer = 0  # 귤의 종류 개수
    cnt = Counter(tangerine).most_common()  # most_common(): 빈도수 기준으로 정렬해주는 Counter의 함수
    
    for _, t in cnt:  
        k -= t  # 수확해야 하는 귤 k가 0이 될 때까지 귤의 개수 t만큼 빼준다
        answer += 1  # 종류 개수도 +1 해준다
        
        if k <= 0:  # k개만큼 수확했으면 for문 탈출
            break
    
    return answer