def solution(numbers):
    # numbers의 요소들을 str로 바꾸기
    numbers = [str(n) for n in numbers]
    
    # numbers의 요소들을 네 번 반복해 내림차순 정렬하기 
    # numbers의 원소는 0이상 1000이하, 모두 네 자리 수 이상으로 만들어 비교하기
    numbers.sort(key=lambda x: x * 4, reverse=True)
    
    # 정답이 0인 경우 0000 -> 이런걸 0으로 나타내기
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
    
    return answer