def solution(s):
    stack = []

    for char in s:
        # 스택의 마지막 문자와 현재 문자가 같으면 제거
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    # 모두 제거되었으면 1, 남아 있으면 0
    return 1 if not stack else 0