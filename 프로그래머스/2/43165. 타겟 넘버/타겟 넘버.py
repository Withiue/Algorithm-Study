# numbers 순서 고정, 각 수들을 더하거나 빼서 타겟 넘버 만들어야 한다.
# 타겟 넘버를 만드는 방법의 수 return하기

# 재귀로 모든 경우의 수 끝에 나온 수가 타겟 넘버와 일치하면 answer += 1

def recur(numbers, target, cur_idx, cur_sum):
    # 멈추는 조건: 타겟 넘버와 일치하면 1, 아니면 0 반환
    if cur_idx == len(numbers):
        return 1 if cur_sum == target else 0
    
    # 재귀 파트: (현재가 +일때의 일치 횟수) + (현재가 -일때의 일치 횟수) 반환
    return (
        recur(numbers, target, cur_idx + 1, cur_sum + numbers[cur_idx])
        + recur(numbers, target, cur_idx + 1, cur_sum - numbers[cur_idx])
    )
    

def solution(numbers, target):
    return recur(numbers, target, 0, 0)