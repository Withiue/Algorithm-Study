# 한 개씩 뽑아 두 수 곱하기
# 이걸 누적합하기
# 누적합이 최소인걸 구하기
# 한 번 뽑은건 다시 뽑을 수 없음

# A, B 정렬, 둘 중 하나는 역순으로 정렬
# 각각의 원소를 정렬된 순서대로 곱해서 누적합 한다

def solution(A,B):
    answer = 0  # 최소 누적합
    A.sort()
    B.sort(reverse=True)
    
    answer = sum([A[i] * B[i] for i in range(len(A))])
    
    return answer