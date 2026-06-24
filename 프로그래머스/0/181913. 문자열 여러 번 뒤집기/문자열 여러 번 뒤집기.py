def solution(my_string, queries):
    
    for s, e in queries:
        original = my_string[s:e+1]  # 자르기
        reverse = original[::-1]  # 뒤집기
        my_string = my_string[:s] + reverse + my_string[e+1:]  # 더하기
    
    return my_string