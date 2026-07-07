# 지금까지 나온적이 없는 수이면 배열 맨 뒤에 추가

def solution(arr, k):  # 무작위 배열 arr, 길이 k
    answer = []
    for x in arr:
        if x not in answer:
            answer.append(x)
        if len(answer) == k: break
    
    if len(answer) != k:
        answer.extend([-1] * (k - len(answer)))
    return answer