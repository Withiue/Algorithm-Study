# indices에 있는 글자들을 ' '로 replace 하고 trim으로 공백들을 없애기

def solution(my_string, indices):
    answer = [c for c in my_string]
    for i in indices:
        answer[i] = ''
    return ''.join(answer)