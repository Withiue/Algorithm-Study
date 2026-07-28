def solution(picture, k):
    result = []
    for line in picture:
        tmp = ''.join([l * k for l in line])  # 가로로 k배 확대
        # 세로로 k배 확대
        for i in range(k):
            result.append(tmp)
    return result