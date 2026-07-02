def solution(myString):
    answer = []
    for s in myString:
        if s == 'a':
            answer.append('A')
        elif s != 'A' and s.isupper():
            answer.append(s.lower())
        else:
            answer.append(s)
    return ''.join(answer)