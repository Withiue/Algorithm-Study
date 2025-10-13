# n: 수의 개수, m: 수열의 길이
n, m = map(int, input().split())

# 주어진 n개의 수 입력
numbers = list(map(int, input().split()))

# 중복 제거를 위해 set으로 변환 후 정렬
numbers = sorted(set(numbers))

# 결과를 저장할 리스트
result = []

def backtracking():
    """백트래킹을 이용한 중복 순열 생성"""
    # 수열의 길이가 m이 되면 출력
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    # 중복을 허용하므로 매번 모든 수를 선택 가능
    for num in numbers:
        result.append(num)  # 현재 수를 수열에 추가
        backtracking()  # 재귀 호출
        result.pop()  # 백트래킹: 마지막 수 제거

# 백트래킹 시작
backtracking()