# n: 수의 개수, m: 수열의 길이
n, m = map(int, input().split())

# 주어진 n개의 수 입력
numbers = list(map(int, input().split()))

# 중복 제거를 위해 set으로 변환 후 정렬
numbers = sorted(set(numbers))

# 결과를 저장할 리스트
result = []

def backtracking(start):
    """백트래킹을 이용한 비내림차순 중복 조합 생성"""
    # 수열의 길이가 m이 되면 출력
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    # start 인덱스부터 끝까지 탐색 (비내림차순 유지)
    for i in range(start, len(numbers)):
        result.append(numbers[i])  # 현재 수를 수열에 추가
        backtracking(i)  # 같은 인덱스부터 시작 (중복 허용)
        result.pop()  # 백트래킹: 마지막 수 제거

# 백트래킹 시작 (인덱스 0부터)
backtracking(0)