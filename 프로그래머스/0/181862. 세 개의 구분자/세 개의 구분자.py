def solution(myStr):
    myStr = myStr.replace("a", " ").replace("b", " ").replace("c", " ").split()
    return ["EMPTY"] if not bool(myStr) else myStr