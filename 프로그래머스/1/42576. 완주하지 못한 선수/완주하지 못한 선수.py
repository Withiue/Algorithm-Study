# Counter로 participant, completion 세기
# participant에서 completion 빼기
# 남은 값 return하기

from collections import Counter

def solution(participant, completion):
    a = Counter(participant) - Counter(completion)
    return list(a)[0]