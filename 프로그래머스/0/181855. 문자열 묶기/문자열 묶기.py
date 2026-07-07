from collections import Counter

def solution(strArr):
    length = [len(s) for s in strArr]
    cnt = Counter(length).most_common()
    return cnt[0][1]
    