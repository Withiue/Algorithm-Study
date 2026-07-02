# 1. X, Y 자릿수 세기
# 2. X, Y 짝꿍 비교하기 -> min값만 남기기, 짝꿍 없으면 -1, 0으로만 구성되어 있으면 0
# 3. 짝꿍으로 가장 큰 정수 만들어 반환하기

def solution(X, Y):
    x_cnt = [0 for _ in range(10)]  # X의 숫자 세기
    y_cnt = [0 for _ in range(10)]  # Y의 숫자 세기
    
    for x in X:
        x_cnt[int(x)] += 1
    
    for y in Y:
        y_cnt[int(y)] += 1
    
    pair_cnt = [min(x_cnt[n], y_cnt[n]) for n in range(10)]
    
    # 짝꿍 없으면 -1 return
    if sum(pair_cnt) == 0:
        return "-1"
    
    # 0으로만 구성되어 있으면 0 return
    if pair_cnt[0] > 0 and sum(pair_cnt[1:]) == 0:
        return "0"
    
    answer = ''
    
    for i in range(10):
        if pair_cnt[i] > 0:
            answer += str(i) * pair_cnt[i]
    
    return answer[::-1]  # 뒤집으면 가장 작은 수 -> 가장 큰 수