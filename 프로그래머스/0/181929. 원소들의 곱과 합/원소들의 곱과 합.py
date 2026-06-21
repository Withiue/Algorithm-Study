def solution(num_list):
    a = 1
    for i in num_list:
        a *= i
        
    b = sum(num_list)
    return 1 if a < b*b else 0