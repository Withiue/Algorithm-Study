def solution(s):
    answer = 0
    n = len(s)

    # 문자열을 왼쪽으로 i칸 회전
    for i in range(n):
        rotated = s[i:] + s[:i]

        stack = []
        is_valid = True

        for bracket in rotated:
            if bracket in "([{":
                stack.append(bracket)
            else:
                # 닫는 괄호인데 앞에 여는 괄호가 없으면 잘못된 문자열
                if not stack:
                    is_valid = False
                    break

                top = stack.pop()

                # 괄호 종류가 맞는지 확인
                if (bracket == ")" and top != "(") or \
                   (bracket == "]" and top != "[") or \
                   (bracket == "}" and top != "{"):
                    is_valid = False
                    break

        # 모든 괄호를 처리한 뒤 stack이 비어 있어야 올바른 문자열
        if is_valid and not stack:
            answer += 1

    return answer