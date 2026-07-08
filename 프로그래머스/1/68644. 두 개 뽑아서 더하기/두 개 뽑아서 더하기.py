# 1. 2개 뽑는 모든 조합으로 더하기
# 2. 더한 값이 기존 answer 리스트에 없으면 추가하기
# 3. answer 오름차순 정렬해서 return하기

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            tmp_num = numbers[i] + numbers[j]
            if tmp_num not in answer:
                answer.append(tmp_num)
    answer.sort()
    return answer