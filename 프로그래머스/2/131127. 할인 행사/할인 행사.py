from collections import Counter

def solution(want, number, discount):
    answer = 0

    # 원하는 상품과 개수
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    # 10일씩 확인
    for i in range(len(discount) - 9):
        # 현재 10일간 할인 상품 개수
        current = Counter(discount[i:i + 10])

        # 원하는 상품 구성이 정확히 맞으면 가입 가능
        if current == Counter(want_dict):
            answer += 1

    return answer