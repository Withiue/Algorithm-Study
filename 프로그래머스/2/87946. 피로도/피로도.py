# 던전 = [입장 가능 최소 체력, 소모 체력]
# 유저가 탐험할 수 있는 최대 던전 수 구하기

# 최대 던전이 8개니까 완전탐색

from itertools import permutations

def solution(k, dungeons):
    max_lst = []
    
    for p in permutations(dungeons):  # 모든 순서 만들기
        tmp_k = k  # 임시 체력
        cnt_d = 0  # 돌은 던전 수
        for min_e, consume_e in p:  # 순서대로 던전 돌기
            # 최소 체력 통과했는가?
            if tmp_k < min_e:
                break
            
            # 소모 피로도 이상의 체력이 남아있는가?
            if tmp_k < consume_e:
                break
                
            # 던전 탐험
            tmp_k -= consume_e
            cnt_d += 1
            
        max_lst.append(cnt_d)
        
    # 가장 많이 탐험한 던전 수 return
    return max(max_lst)