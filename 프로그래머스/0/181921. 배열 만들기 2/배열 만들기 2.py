def solution(l, r):
    result = []
    
    for i in range(l, r + 1):
        if i % 5 == 0:
            string = str(i)

            # string에서 0과 5를 없애서 ''이면 result에 넣기
            string = string.replace('0', '')  # replace()는 새로운 문자열을 반환할 뿐 원본을 수정하지 않는다.
            string = string.replace('5', '')

            if string == '':
                result.append(i)
    
    # result에 아무것도 없으면 return [-1]
    return result if result else [-1]