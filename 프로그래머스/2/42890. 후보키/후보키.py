from itertools import combinations

def solution(relation):
    col_len = len(relation[0])
    row_len = len(relation)

    candidate_keys = []

    # 컬럼 1개짜리부터 전체 컬럼까지 확인
    for cnt in range(1, col_len + 1):

        # cnt개 컬럼 조합 만들기
        for cols in combinations(range(col_len), cnt):

            # ----------------
            # 1. 최소성 확인
            # ----------------
            is_minimal = True

            for key in candidate_keys:
                # 기존 후보키가 현재 조합 안에 들어있다면
                if set(key).issubset(set(cols)):
                    is_minimal = False
                    break

            if not is_minimal:
                continue

            # ----------------
            # 2. 유일성 확인
            # ----------------
            values = set()

            for i in range(row_len):
                tmp = []

                for col in cols:
                    tmp.append(relation[i][col])

                values.add(tuple(tmp))

            # 모든 행이 서로 다르다면 후보키
            if len(values) == row_len:
                candidate_keys.append(cols)

    return len(candidate_keys)