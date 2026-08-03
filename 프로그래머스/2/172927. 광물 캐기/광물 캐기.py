# 피로도 최소값 구하기
# 피로도 표를 만들기
# minerals를 5개씩 끊어서 1. 다이아몬드 2. 철 3. 돌 순으로 그룹들을 정렬하기
# 최소 피로도를 energy에 더하기

from collections import Counter

def solution(picks, minerals):  # picks[dia, iron, stone]
    energy = 0
    
    # 피로도 표
    e_board = [
        [1, 1, 1],  # 다이아 곡괭이
        [5, 1, 1],  # 철 곡괭이
        [25, 5, 1]  # 돌 곡괭이
    ]
    
    # 곡괭이로 캘 수 있는 최대 광물까지만 자르기
    minerals = minerals[:sum(picks)*5]
    
    # 5개씩 슬라이싱 하기
    groups = []
    for i in range(0, len(minerals), 5):
        mineral = minerals[i:i+5]
        cnt = Counter(mineral)
        
        groups.append([
            cnt['diamond'],
            cnt['iron'],
            cnt['stone']
        ])
    
    # 정렬하기
    groups.sort(key=lambda x: (x[0], x[1]), reverse=True)
    
    # 곡괭이 좋은거부터 쓰기
    for group in groups:
        for pick_idx in range(3):
            if picks[pick_idx] > 0:
                picks[pick_idx] -= 1
                
                energy += group[0] * e_board[pick_idx][0] + group[1] * e_board[pick_idx][1] + group[2] * e_board[pick_idx][2]
                break
    
    return energy