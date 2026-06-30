def solution(str_list):
    for i, c in enumerate(str_list):
        if c == "l":  # l이 먼저 나왔으면 왼쪽에 있는 문자열 리스트 return
            return str_list[:i]
        elif c == "r":  # r이 먼저 나왔으면 왼쪽에 있는 문자열 리스트 return
            return str_list[i+1:]
    else:  # l이나 r이 없다면 빈 리스트 return
        return []
            