# 1. char 하나씩 순회
# 2. 해당 문자를 아스키 코드로 전환
# 3. 아스키 코드를 가공해서 대문자, 소문자 순으로 answer의 해당 인덱스에 +1 하기

def solution(my_string):
    answer = [0] * 52
    
    for c in my_string:
        ascii_c = ord(c)
        if ascii_c < 97:  # 대문자면
            answer[ascii_c - 65] += 1   
        else:  # 소문자면
            answer[ascii_c - 97 + 26] += 1   
    return answer