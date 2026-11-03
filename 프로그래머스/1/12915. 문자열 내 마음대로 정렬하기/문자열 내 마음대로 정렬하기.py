def solution(strings, n):
    # 첫 번째로 n번째 인덱스 기준 정렬, 두 번째로 사전순 앞선 문자열 정렬
    answer = sorted(strings, key=lambda x:(x[n], x))
    return answer