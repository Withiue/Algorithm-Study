def solution(myString, pat):
    result = 0
    for i in range(len(myString) - len(pat) + 1):
        if myString[i:i+len(pat)] == pat:
            result += 1
    return result