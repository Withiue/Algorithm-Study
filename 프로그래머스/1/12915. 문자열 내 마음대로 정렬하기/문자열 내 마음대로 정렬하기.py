def solution(strings, n):
    # 인덱스 순으로 정렬
    # 매개변수 x에 대해 1순위는 x[n], 2순위는 x로 sorting 한다
    strings.sort(key=lambda x : (x[n], x))
    
    return strings