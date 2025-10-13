def backtracking(start, depth):
    """백트래킹을 이용한 조합 생성"""
    # 6개를 모두 선택했으면 출력
    if depth == 6:
        print(' '.join(map(str, result)))
        return
    
    # start 인덱스부터 끝까지 탐색
    for i in range(start, len(s)):
        result.append(s[i])  # 현재 수를 선택
        backtracking(i + 1, depth + 1)  # 다음 인덱스부터 탐색
        result.pop()  # 백트래킹: 선택 취소

while True:
    # 입력 받기
    data = list(map(int, input().split()))
    k = data[0]  # 집합 S의 크기
    
    # k가 0이면 종료
    if k == 0:
        break
    
    s = data[1:]  # 집합 S의 원소들
    result = []  # 선택된 수들을 저장할 리스트
    
    # 백트래킹 시작
    backtracking(0, 0)
    
    # 각 테스트 케이스 사이에 빈 줄 출력
    print()