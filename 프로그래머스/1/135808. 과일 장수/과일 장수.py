# 사과 1~k점
# 상자당 사과 m개
# 한상자 가격 = 가장 낮은 사과점수 p * m개
# 많은 사과, 최대 이익

# 내림차순 정렬
# 상자 슬라이싱 담기
# m개 중 min으로 한 상자 가격 책정

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)  # 내림차순 정렬
    for i in range(0, len(score), m):
        box = score[i:i+m]  # m개 만큼 슬라이싱
        if len(box) == m:  # 한 상자에 사과 m개 채워지면 팔기
            answer += min(box) * m
        
    return answer