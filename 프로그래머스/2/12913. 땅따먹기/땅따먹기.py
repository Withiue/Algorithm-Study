def solution(land):
    for i in range(1, len(land)):
        for j in range(4):

            prev_max = 0

            # 이전 행의 4칸 확인
            for k in range(4):
                
                # 같은 열은 선택할 수 없음
                if k == j:
                    continue
                
                # 같은 열이 아닌 값들 중 최댓값 찾기
                if land[i - 1][k] > prev_max:
                    prev_max = land[i - 1][k]

            # 현재 칸 + 이전 행에서 선택 가능한 최대값
            land[i][j] += prev_max

    return max(land[-1])