from itertools import combinations

def solution(numbers):
    answer = set()
    
    for a, b in list(combinations(numbers, 2)):
        answer.add(a + b)
    
    answer = list(answer)
    answer.sort()
    
    return answer