def solution(number, k):
    answer = []  # 스택 역할

    for c in number:
        # 1. 스택이 비어 있지 않고
        # 2. 아직 제거할 횟수 k가 남아 있고
        # 3. 스택의 마지막 숫자가 현재 숫자보다 작으면 제거
        while answer and k > 0 and answer[-1] < c:
            answer.pop()
            k -= 1

        answer.append(c)

    # 예외 처리: k가 남은 경우
    # 예: number = "987", k = 1
    # 내림차순이라 앞에서 제거되지 않았으므로 뒤에서 k개 제거
    if k > 0:
        answer = answer[:-k]

    return ''.join(answer)