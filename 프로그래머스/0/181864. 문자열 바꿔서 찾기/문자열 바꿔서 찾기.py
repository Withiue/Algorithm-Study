def solution(myString, pat):
    r_mystr = ''.join(["B" if s == "A" else "A" for s in myString])
    return int(pat in r_mystr)