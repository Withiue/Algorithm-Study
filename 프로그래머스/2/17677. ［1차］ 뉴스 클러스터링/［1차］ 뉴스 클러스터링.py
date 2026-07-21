from collections import Counter

def solution(str1, str2):
    
    # 대문자와 소문자의 차이는 무시한다.
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다.
    A = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            A.append(str1[i:i+2])
    A = Counter(A)
    
    B = []
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            B.append(str2[i:i+2])
    B = Counter(B)
    
    # J()
    inter = A & B
    plus = A | B
    
    len_inter = sum(inter.values())
    len_plus = sum(plus.values())
    
    # 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
    if len_inter == 0 and len_plus == 0:
        return 1 * 65536
    else:
        return int(65536 * (len_inter / len_plus))